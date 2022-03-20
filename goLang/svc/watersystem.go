package svc

import (
	"fmt"
	"github.com/stianeikeland/go-rpio/v4"
	"gopkg.in/yaml.v3"
	"io/ioutil"
	"log"
	"strconv"
	"time"

	gomail "gopkg.in/mail.v2"
)

const (
	// ResponseComplete ...
	ResponseComplete = "time is complete"
)

// EmailDetails ...
type EmailDetails struct {
	EmailNotificationSender    string `yaml:"emailNotificationSender"`
	EmailNotificationRecipient string `yaml:"emailNotificationRecipient"`
	EmailNotificationSubject   string `yaml:"emailNotificationSubject"`
}

// countdown ...
type countdown struct {
	t int
	m int
	s int
}

// InitializeWaterFlow will deliver signal for output for the allocated time of service.
func InitializeWaterFlow(channel string, waterTime string) {

	var waterDetails WaterDetails
	waterOutputVals, err := waterDetails.GetWaterDetails()
	if err != nil {
		log.Fatalln(err)
	}

	var weeklyWaterCapacity = (waterOutputVals.AverageWaterRequiredLawn / waterOutputVals.AverageWaterOutput) * 60 // to minutes

	if waterTimeInt, waterParseErr := strconv.ParseFloat(waterTime, 32); waterParseErr == nil {
		var dailyWaterCapacity = (weeklyWaterCapacity / float32(waterTimeInt)) * 60

		// countDown begins from here
		pinErr := rpio.Open()
		if pinErr != nil {
			log.Fatal(pinErr)
		}

		var channelInt, parseErr = strconv.Atoi(channel)
		if parseErr != nil {
			log.Fatal(err)
		}

		var waterTimeAdjuster = time.Now().Local().Add(time.Hour*time.Duration(0) +
			time.Minute*time.Duration(dailyWaterCapacity) + time.Second*time.Duration(0))

		pin := rpio.Pin(channelInt)
		pin.Output()
		pin.Low()

		for i := waterTimeInt; i >= 0; i-- {

			for range time.Tick(1 * time.Second) {
				var remainingTime = getTimeRemaining(waterTimeAdjuster)
				if remainingTime.t <= 0 {
					fmt.Print(ResponseComplete)
					break
				}

				fmt.Printf("minutes : %d seconds : %d \n", remainingTime.m, remainingTime.s)
			}
		}
		pin.High()

		var rpioErr = rpio.Close()
		if rpioErr != nil {
			log.Fatal(rpioErr)
		}
	}
}

// NotifyClient to notify the client of the work complete
func (emailDetails *EmailDetails) NotifyClient(clientInfo ClientInformation, details CurrentWeather) {

	yamlFile, err := ioutil.ReadFile("config.yaml")
	if err != nil {
		log.Fatal(FileNotFoundErr)

	}

	var emailAddressErr = yaml.Unmarshal(yamlFile, &emailDetails)
	if emailAddressErr != nil {
		log.Fatal(err)
	}

	var mail = gomail.NewMessage()
	mail.SetHeader("From", emailDetails.EmailNotificationSender)
	mail.SetHeader("To", emailDetails.EmailNotificationRecipient)
	mail.SetHeader("Subject", emailDetails.EmailNotificationSubject)

	var bodymessage = fmt.Sprintf("current time : %v \n, city : %v \n, description : %v \n\n"+
		"current temperature : %v \n, current humidity : %v, \n, current wind speed : %v \n\n,"+
		time.Now().String(), clientInfo.CityName, details.WeatherDesc, details.Temperature, details.Humidity,
		details.WindSpeed)

	mail.SetBody("text/plain", bodymessage)

	var dailer = gomail.NewDialer("smtp.gmail.com", 587, emailDetails.EmailNotificationSender, "password")
	if err := dailer.DialAndSend(mail); err != nil {
		log.Fatal(err)
	}
}

// getTimeRemaining returns the remaining time
func getTimeRemaining(t time.Time) countdown {
	var currentTime = time.Now()
	var diff = t.Sub(currentTime)

	var total = int(diff.Seconds())
	var minutes = int(total/60) % 60
	var seconds = int(total % 60)

	return countdown{
		t: total,
		m: minutes,
		s: seconds,
	}

}

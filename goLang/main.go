package main

import (
	"github.com/mohit2530/LawnSprinklerSystem/goLang/svc"
	"log"
	"time"
)

func main() {

	var clientInfo svc.ClientInformation
	clientDetails, err := clientInfo.GetClientInfo()
	if err != nil {
		log.Fatal(err)
	}
	clientDetails.CurrentTime = time.Now()

	weatherDetails, err := svc.BuildWeatherDataCSV(clientDetails)
	if err != nil {
		log.Fatal(err)
	}

	if weatherDetails != nil {
		svc.InitializeWaterFlow(clientDetails.Channel, clientDetails.WaterTime)
		var currentWeather = svc.CurrentWeather{
			City:        weatherDetails.City,
			Weather:     weatherDetails.Weather,
			WeatherDesc: weatherDetails.WeatherDesc,
			Temperature: weatherDetails.Temperature,
			Humidity:    weatherDetails.Humidity,
			WindSpeed:   weatherDetails.WindSpeed,
		}

		var emailDetails svc.EmailDetails
		emailDetails.NotifyClient(clientInfo, currentWeather)

	}
}

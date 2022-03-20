package svc

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

const (
	AppId                   = "appid="
	DefaultMeasurementUnit  = "&units=imperial"
	FileName                = "weatherData.csv"
	ErrorWritingDataToCSV   = "error in writing data to the CSV file"
	ErrorUnmarshallingToCSV = "error during unmarshalling to the CSV file"
)

//WeatherDetails ...
type WeatherDetails struct {
	Coord struct {
		Lon float64 `json:"lon"`
		Lat float64 `json:"lat"`
	} `json:"coord"`
	Weather []struct {
		Id          int    `json:"id"`
		Main        string `json:"main"`
		Description string `json:"description"`
		Icon        string `json:"icon"`
	} `json:"weather"`
	Base string `json:"base"`
	Main struct {
		Temp      float64 `json:"temp"`
		FeelsLike float64 `json:"feels_like"`
		TempMin   float64 `json:"temp_min"`
		TempMax   float64 `json:"temp_max"`
		Pressure  int     `json:"pressure"`
		Humidity  int     `json:"humidity"`
	} `json:"main"`
	Visibility int `json:"visibility"`
	Wind       struct {
		Speed int `json:"speed"`
		Deg   int `json:"deg"`
	} `json:"wind"`
	Clouds struct {
		All int `json:"all"`
	} `json:"clouds"`
	Dt  int `json:"dt"`
	Sys struct {
		Type    int    `json:"type"`
		Id      int    `json:"id"`
		Country string `json:"country"`
		Sunrise int    `json:"sunrise"`
		Sunset  int    `json:"sunset"`
	} `json:"sys"`
	Timezone int    `json:"timezone"`
	Id       int    `json:"id"`
	Name     string `json:"name"`
	Cod      int    `json:"cod"`
}

// GetWeatherData returns the weather data of the client location
func (weatherData *WeatherDetails) GetWeatherData(client *ClientInformation) (*CurrentWeather, error) {

	var currentWeatherDetails, err = BuildWeatherDataCSV(client)
	if err != nil {
		log.Fatal(ErrorWritingDataToCSV)
		return nil, err
	}
	logWeatherDetailsToCsv(currentWeatherDetails)
	return nil, nil
}

// CurrentWeather ...
type CurrentWeather struct {
	City        string
	Weather     string
	WeatherDesc string
	Temperature float64
	Humidity    int
	WindSpeed   int
}

// fmtToString converts current weather data to string format
func (currentWeather *CurrentWeather) fmtToString() string {

	var toString = fmt.Sprintf("%10v %10v %20v %10v %10v %10v",
		currentWeather.City, currentWeather.Weather, currentWeather.WeatherDesc, currentWeather.Temperature,
		currentWeather.Humidity, currentWeather.WindSpeed)
	return toString

}

// logWeatherDetailsToCsv to log data to the CSV file
func logWeatherDetailsToCsv(currentWeatherDetails *CurrentWeather) {

	file, err := os.OpenFile(FileName, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatal(ErrorWritingDataToCSV)

	}

	defer file.Close()
	_, err2 := file.WriteString(currentWeatherDetails.fmtToString() + "\n")
	if err2 != nil {
		log.Fatal(ErrorWritingDataToCSV)
	}

}

// BuildWeatherDataCSV returns the weather data to write on CSV
func BuildWeatherDataCSV(client *ClientInformation) (*CurrentWeather, error) {

	var oddHours = make([]int, 0)
	for i := 0; i < 24; i = i + 2 {
		oddHours = append(oddHours, i)
	}
	var currentWeatherDetails = CurrentWeather{}
	for i := 0; i < len(oddHours); i++ {
		if client.CurrentTime.Hour() == i {

			var svcProps = client.BaseUri + AppId + client.ApiKey + "&q=" + client.CityName + DefaultMeasurementUnit

			resp, err := http.Get(svcProps)
			if err != nil {
				log.Fatal(ErrorWritingDataToCSV)
				return nil, err
			}
			data, err := ioutil.ReadAll(resp.Body)
			if err != nil {
				log.Fatal(ErrorUnmarshallingToCSV)
				return nil, err
			}

			var weatherDetails WeatherDetails
			json.Unmarshal(data, &weatherDetails)
			currentWeatherDetails.City = weatherDetails.Name
			currentWeatherDetails.WindSpeed = weatherDetails.Wind.Speed
			currentWeatherDetails.Temperature = weatherDetails.Main.Temp
			currentWeatherDetails.Humidity = weatherDetails.Main.Humidity
			currentWeatherDetails.Weather = weatherDetails.Weather[0].Main
			currentWeatherDetails.WeatherDesc = weatherDetails.Weather[0].Description
		}

	}
	return &currentWeatherDetails, nil
}

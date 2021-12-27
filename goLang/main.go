package main

import (
	"fmt"
	userinfo "github.com/mohit2530/LawnSprinklerSystem/goLang/service/userInfo"
	"github.com/mohit2530/LawnSprinklerSystem/goLang/service/utility"
	"github.com/mohit2530/LawnSprinklerSystem/goLang/service/weatherApi"
)

func main() {

	utility.WelcomeMessage()
	userDetails := userinfo.BuildUserInfo()

	cityName := userDetails.City
	weatherDetails := weatherApi.BuildWeatherDetails(cityName)
	sanitizedData := FormatWeather(weatherDetails)
	utility.SaveFile(sanitizedData)
}

// FormatWeather function formats the weather data into a single line of string
func FormatWeather(weatherDetails weatherApi.WeatherDetails) (formattedData string) {

	currentTemp := fmt.Sprintf("%.2f", weatherDetails.Main.Temp)
	currentHumidity := fmt.Sprintf("%d", weatherDetails.Main.Humidity)
	currentWindSpeed := fmt.Sprintf("%d", weatherDetails.Wind.Speed)
	formattedData = fmt.Sprintf("%10v %10v %20v %10v %10v %10v", weatherDetails.Name, weatherDetails.Weather[0].Main, weatherDetails.Weather[0].Description, currentTemp, currentHumidity, currentWindSpeed)
	return formattedData
}

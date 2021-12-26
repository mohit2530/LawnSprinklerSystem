package weatherApi

import (
	"encoding/json"
	"fmt"
	"github.com/mohit2530/LawnSprinklerSystem/goLang/service/utility"
)

// BuildWeatherDetails function
func BuildWeatherDetails(nameOfCity string) (weatherInfo WeatherDetails) {

	svcPropsUri := buildWeatherUri(nameOfCity)
	data, err := WeatherRouter(svcPropsUri)
	if err != nil {
		return
	}
	var weatherDetails WeatherDetails
	json.Unmarshal(data, &weatherDetails)
	fmt.Println(weatherDetails)
	return weatherDetails
}

func buildWeatherUri(nameOfCity string) string {

	svcProps := utility.BaseUri + utility.ApplicationId + utility.ApiKey + utility.UniqueId + nameOfCity + utility.UnitsOfMeasurement
	fmt.Println(svcProps)
	return svcProps
}

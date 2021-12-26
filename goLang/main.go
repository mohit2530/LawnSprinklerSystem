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
	fmt.Println(userDetails, weatherDetails)

}

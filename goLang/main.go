package main

import (
	"github.com/mohit2530/LawnSprinklerSystem/goLang/downstream"
	"github.com/mohit2530/LawnSprinklerSystem/goLang/service/utility"
)

func main() {

	utility.WelcomeMessage()
	values, _ := downstream.BuildUserInfo()
	downstream.BuildWeatherInfoRequest(values)
}

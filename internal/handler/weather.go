package handler

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"

	"github.com/mohit2530/LawnSprinklerSystem/internal/model"
)

func GetSystemHealth(rw http.ResponseWriter, r *http.Request) {

	var weather model.Weather

	populateWeatherDetails(&weather)

	rw.WriteHeader(http.StatusOK)
	rw.Header().Add("Content-Type", "application-json")
	json.NewEncoder(rw).Encode(weather)
}

func populateWeatherDetails(*model.Weather) {

	url := "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m"

	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Read error:", err)
		return
	}

	fmt.Println(string(body))

}

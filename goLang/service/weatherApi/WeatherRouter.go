package weatherApi

import (
	"io/ioutil"
	"log"
	"net/http"
)

// WeatherRouter function calls the weather api and
// returns the value based on the request and handles
// error if it is prevalent
func WeatherRouter(baseUri string) ([]byte, error) {

	response, err := http.Get(baseUri)
	if err != nil {
		log.Fatalln("internal server exception")
		return nil, err
	}
	data, err := ioutil.ReadAll(response.Body)
	if err != nil {
		log.Fatalln("Exception while parsing data")
		return nil, err
	}
	return data, nil

}

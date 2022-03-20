package svc

import (
	"io/ioutil"
	"log"
	"time"

	"gopkg.in/yaml.v3"
)

const (
	FileNotFoundErr = "error in locating file"
)

// ClientInformation ...
type ClientInformation struct {
	ApiKey      string `yaml:"ApiKey"`
	BaseUri     string `yaml:"BaseUri"`
	Channel     string `yaml:"Channel"`
	CityName    string `yaml:"Cityname"`
	WaterTime   string `yaml:"Watertime"`
	CurrentTime time.Time
}

// GetClientInfo to retrieve the client information
func (client *ClientInformation) GetClientInfo() (*ClientInformation, error) {

	yamlFile, err := ioutil.ReadFile("config.yaml")
	if err != nil {
		log.Fatal(FileNotFoundErr)
		return client, err
	}

	var clientDataErr = yaml.Unmarshal(yamlFile, &client)
	if clientDataErr != nil {
		log.Fatal(err)
		return client, err
	}
	return client, nil
}

// WaterDetails ...
type WaterDetails struct {
	AverageWaterOutput       float32 `yaml:"averageWaterOutput"`
	AverageWaterRequiredLawn float32 `yaml:"averageWaterRequiredLawn"`
}

// GetWaterDetails to retrieve the water details
func (waterDetails *WaterDetails) GetWaterDetails() (*WaterDetails, error) {

	yamlFile, err := ioutil.ReadFile("config.yaml")
	if err != nil {
		log.Fatal(FileNotFoundErr)
		return waterDetails, err
	}

	var waterDetailsErr = yaml.Unmarshal(yamlFile, &waterDetails)
	if waterDetailsErr != nil {
		log.Fatal(err)
		return waterDetails, err
	}
	return waterDetails, nil

}

package userinfo

import (
	"bufio"
	"errors"
	downstream "github.com/mohit2530/LawnSprinklerSystem/goLang/model"
	uuid "github.com/nu7hatch/gouuid"
	"log"
	"os"
	"strings"
)

// BuildUserInfo function to build the user request and
// allow user to input variables, use of uuid.v4()
func BuildUserInfo() (userInfo downstream.UserInfo) {

	userInput := RequestUserInfo()

	userId, err := uuid.NewV4()

	if err != nil {
		log.Fatalln("Internal Server Exception")
		return
	}

	userDetails := downstream.UserInfo{
		Id:           userId.String(),
		FirstName:    userInput[1],
		City:         userInput[2],
		EmailAddress: userInput[3],
		ZipCode:      userInput[4],
	}

	return userDetails
}

// RequestUserInfo method is used to request
// client information to feed to the system
func RequestUserInfo() []string {

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	userInput := scanner.Text()
	userDetails, err := parseMsg(&userInput)
	if err != nil {
		log.Fatalln("Invalid User Parameter. Exiting the application.")
		return nil
	}
	return userDetails

}

// parseMsg function to parse the user input string
func parseMsg(userInput *string) ([]string, error) {

	if len(*userInput) == 0 {
		return nil, errors.New("invalid operation")
	}
	parsedMessage := strings.Split(*userInput, "-")
	if parsedMessage[1] == "" || parsedMessage[2] == "" || parsedMessage[3] == "" {
		return nil, errors.New("name, email and city is required")
	}
	return parsedMessage, nil
}

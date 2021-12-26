package userinfo

import (
	"bufio"
	"errors"
	"log"
	"os"
	"strings"
)

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

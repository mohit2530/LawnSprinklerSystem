package downstream

import (
	userinfo "github.com/mohit2530/LawnSprinklerSystem/goLang/service/userInfo"
	uuid "github.com/nu7hatch/gouuid"
	"log"
)

type UserInfo struct {
	Id           string
	FirstName    string
	EmailAddress string
	ZipCode      string
}

func BuildUserInfo() (UserInfo, error) {

	userInput := userinfo.RequestUserInfo()

	userId, err := uuid.NewV4()

	if err != nil {
		log.Fatalln("Internal Server Exception")
		return UserInfo{}, nil
	}

	userDetails := UserInfo{
		Id:           userId.String(),
		FirstName:    userInput[1],
		EmailAddress: userInput[2],
		ZipCode:      userInput[3],
	}

	return userDetails, nil
}

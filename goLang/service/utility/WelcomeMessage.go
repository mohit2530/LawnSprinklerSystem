package utility

import "fmt"

// WelcomeMessage function greets the user
func WelcomeMessage() {

	fmt.Println(" ")
	fmt.Printf("================================= LANW SPRINKLER SYSTEM =========================== \n")
	fmt.Println(" ")
	fmt.Printf("Use '-' to fill in values. \t -name, -city, -emailAddress -zip \n")
	fmt.Printf("Use -help for support. \n")
}

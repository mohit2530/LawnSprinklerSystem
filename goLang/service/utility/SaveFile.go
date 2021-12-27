package utility

import "os"

// SaveFile function saves the data to the file
func SaveFile(data string) bool {

	file, err := os.OpenFile("informationData.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		panic("cannot save data")
		return false

	}

	defer file.Close()
	_, err2 := file.WriteString(data + "\n")
	if err2 != nil {
		panic("cannot write to file. permission denied")
		return false
	}
	return true

}

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parsePuzzleInputToIntArray(file *os.File) []int {
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var numberArray []int
	for scanner.Scan() {
		//Split on new Line and grab the number, just to convert it from ascii to int.
		tempNumberString := strings.Split(scanner.Text(), "\n")[0]
		temp, err := strconv.Atoi(tempNumberString)
		if err != nil {
			fmt.Printf("failed to convert number %s", err)
			os.Exit(1)
		}
		numberArray = append(numberArray, temp)
	}
	return numberArray
}

func countIncreasementOfPairs(numberArray []int) int {
	count := 0
	for i := 0; i < len(numberArray); i++ {
		if (i == 0 || i != len(numberArray)-1) && (numberArray[i+1] > numberArray[i]) {
			count++
		}
	}
	return count
}

func convertToThreeMeasurementSum(numberArray []int) []int {
	var newArray []int
	for i := 0; i < len(numberArray); i++ {
		if i != len(numberArray)-1 && i != len(numberArray)-2 {
			threeMeasurementSum := numberArray[i] + numberArray[i+1] + numberArray[i+2]
			newArray = append(newArray, threeMeasurementSum)
		}
	}
	return newArray
}

func main() {
	file, err := os.Open("PuzzleInput")

	if err != nil {
		fmt.Printf("failed to convert number %s", err)
		os.Exit(1)
	}
	numberArray := parsePuzzleInputToIntArray(file)
	file.Close()

	newArray := convertToThreeMeasurementSum(numberArray)
	count := countIncreasementOfPairs(newArray)
	fmt.Print(count)
}

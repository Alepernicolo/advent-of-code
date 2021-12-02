package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func calculateMovement(textArray []string) (int, int) {
	horizontalPos := 0
	depth := 0
	aim := 0
	for _, movementString := range textArray {
		movementPair := strings.Split(movementString, " ")
		direction := movementPair[0]
		directionUnit, err := strconv.Atoi(movementPair[1])

		if err != nil {
			fmt.Printf("Fatal, String could not be converted to Int")
			os.Exit(1)
		}

		switch direction {
		case "forward":
			horizontalPos += directionUnit
			depth += (aim * directionUnit)
		case "up":
			aim -= directionUnit
		case "down":
			aim += directionUnit
		}
	}
	return horizontalPos, depth
}

func parsePuzzleInputToArray(file *os.File) []string {
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var textArray []string
	for scanner.Scan() {
		movementString := strings.Split(scanner.Text(), "\n")[0]
		textArray = append(textArray, movementString)
	}

	return textArray
}

func main() {
	file, err := os.Open("PuzzleInput")

	if err != nil {
		fmt.Printf("failed to open file %s", err)
		os.Exit(1)
	}
	textArray := parsePuzzleInputToArray(file)
	file.Close()

	horizontalPos, depth := calculateMovement(textArray)
	product := horizontalPos * depth
	fmt.Print(product)
}

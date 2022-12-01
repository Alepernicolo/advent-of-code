package main

import (
	aocHelper "aoc/2021/helper"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	puzzleInput := aocHelper.GetPuzzleInput(1)
	greatestCaloriesSum := getGreatestCaloriesSum(puzzleInput)

	fmt.Printf("%d\n", greatestCaloriesSum)

	fmt.Printf("%d", part2(puzzleInput))
}

func getGreatestCaloriesSum(puzzleInput string) int {
	splitPuzzleInput := strings.Split(puzzleInput, "\n\n")
	currentlyGreatestCaloriesSum := 0
	for i := 0; i < len(splitPuzzleInput); i++ {
		caloriesElement := splitPuzzleInput[i]
		caloriesElementSlice := strings.Split(caloriesElement, "\n")
		caloriesSum := sumOf(caloriesElementSlice)
		if caloriesSum > currentlyGreatestCaloriesSum {
			currentlyGreatestCaloriesSum = caloriesSum
		}
	}
	return currentlyGreatestCaloriesSum
}

func part2(puzzleInput string) int {
	newSlice := strings.Split(puzzleInput, "\n\n")
	threeGreatest := 0
	for i := 0; i < 3; i++ {
		currentlyGreatestCaloriesSum, indexAtGreatest := getCurrentGreatest(newSlice)
		newSlice = remove(newSlice, indexAtGreatest)
		threeGreatest += currentlyGreatestCaloriesSum
	}
	return threeGreatest
}

func getCurrentGreatest(splitPuzzleInput []string) (int, int) {
	currentlyGreatestCaloriesSum := 0
	indexAtGreatest := 0
	for i := 0; i < len(splitPuzzleInput); i++ {
		caloriesElement := splitPuzzleInput[i]
		caloriesElementSlice := strings.Split(caloriesElement, "\n")
		caloriesSum := sumOf(caloriesElementSlice)

		if caloriesSum > currentlyGreatestCaloriesSum {
			currentlyGreatestCaloriesSum = caloriesSum
			indexAtGreatest = i
		}
	}
	return currentlyGreatestCaloriesSum, indexAtGreatest
}

func remove(slice []string, s int) []string {
	return append(slice[:s], slice[s+1:]...)
}

func sumOf(slice []string) int {
	sum := 0
	for i := 0; i < len(slice); i++ {
		if slice[i] != "" {
			integer, err := strconv.Atoi(slice[i])
			if err != nil {
				fmt.Printf("Conversion failed")
				fmt.Printf("%d\n%d\n", len(slice), i)
				os.Exit(1)
			}
			sum += integer
		}
	}
	return sum
}

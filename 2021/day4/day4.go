package main

import (
	aocHelper "aoc/2021/helper"
	"fmt"
	"strconv"
	"strings"
)

type bingoNumber struct {
	number int
	marked bool
}

func newBingoNumber(number int) *bingoNumber {
	bn := bingoNumber{number: number}
	bn.marked = false
	return &bn
}

func transformInputToBoard(board [][]int) [][]bingoNumber {
	var bingoBoard [][]bingoNumber
	for _, row := range board {
		var bingoRow []bingoNumber
		for _, rowElement := range row {
			bingoRow = append(bingoRow, *newBingoNumber(rowElement))
		}
		bingoBoard = append(bingoBoard, bingoRow)
	}
	return bingoBoard
}

func transformInputToIntBoard(input string) [][]int {
	var intBoard [][]int
	var tempString [][]string
	splitInput := strings.Split(input, "\n")
	for _, v := range splitInput {
		tempString = append(tempString, strings.Split(v, " "))
	}

	fmt.Print()
	for _, row := range tempString {
		var rowInt []int
		for _, rowElement := range row {
			if rowElement != "" {
				tempInt, _ := strconv.Atoi(rowElement)
				rowInt = append(rowInt, tempInt)
			}
		}
		intBoard = append(intBoard, rowInt)
	}
	return intBoard
}

func convertStringArrayToIntArray(x []string) []int {
	var intArray []int
	for _, v := range x {
		converted, _ := strconv.Atoi(v)
		intArray = append(intArray, converted)
	}
	return intArray
}

func evaluateBoard(currElement bingoNumber, bingoBoard [][]bingoNumber) {
	//iterate
}

func foo(drawnNumbers []int, bingoBoard [][]bingoNumber) {
	for _, currDraw := range drawnNumbers {
		for _, bingoRow := range bingoBoard {
			for _, bingoElement := range bingoRow {
				if currDraw == bingoElement.number {
					bingoElement.marked = true
				}
			}
		}
	}
}

func main() {
	puzzleInput := aocHelper.GetPuzzleInput(4)
	splitInput := strings.Split(puzzleInput, "\n\n")
	stringDrawnNumbers := strings.Split(splitInput[0], ",")
	drawnNumbers := convertStringArrayToIntArray(stringDrawnNumbers)
	fmt.Print(drawnNumbers)

	//3 Dimensional Array of bingoboards
	var bingoBoards [][][]bingoNumber
	for i := 1; i < len(splitInput); i++ {
		intBoard := transformInputToIntBoard(splitInput[i])
		bingoBoard := transformInputToBoard(intBoard)
		//bingoBoards = append(bingoBoards, bingoBoard)
		foo(drawnNumbers, bingoBoard)
	}

	fmt.Print(bingoBoards)

}

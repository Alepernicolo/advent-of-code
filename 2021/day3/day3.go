package main

import (
	aocHelper "aoc/2021/helper"
	"fmt"
	"strings"
)

func main() {
	puzzleInput := aocHelper.GetPuzzleInput(2)
	splitInput := strings.Split(puzzleInput, "\n")
	fmt.Print(splitInput)
}

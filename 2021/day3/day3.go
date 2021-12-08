package main

import (
	aocHelper "aoc/2021/helper"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

const (
	mostCommon  = 0
	leastCommon = 1
)

func convertArrayToDecimal(array []uint8) int {
	// Convert uint8 array that contains binary numbers to decimal
	decimalNumber := 0
	exponent := 0
	for k := len(array) - 1; k >= 0; k-- {
		if array[k] == 1 {
			decimalNumber = decimalNumber + int(math.Pow(2, float64(exponent)))
		}
		exponent++
	}
	return decimalNumber
}

func convertToOneComplement(array []uint8) []uint8 {
	var newArray []uint8
	for _, v := range array {
		if v == 0 {
			newArray = append(newArray, 1)
		} else {
			newArray = append(newArray, 0)
		}
	}
	return newArray
}

func calculatePowerConsumption(slice [][]uint8) int {
	var gammaRateArray []uint8
	for i := 0; i < 12; i++ {
		countZero := 0
		countOne := 0

		for j := 0; j < len(slice)-1; j++ {
			if slice[j][i] == 0 {
				countZero += 1
			} else {
				countOne += 1
			}
		}

		if countZero > countOne {
			gammaRateArray = append(gammaRateArray, 0)
		} else {
			gammaRateArray = append(gammaRateArray, 1)
		}
	}
	// 1 Komplement of gamma Rate is epsilon Rate
	epsilonRateArray := convertToOneComplement(gammaRateArray)
	epsilonRate := convertArrayToDecimal(epsilonRateArray)
	gammaRate := convertArrayToDecimal(gammaRateArray)

	solution := epsilonRate * gammaRate

	return solution
}

func convertInputToMatrix(array []string) [][]uint8 {
	a := make([][]uint8, len(array)-1)
	for i := range a {
		a[i] = make([]uint8, 12)
	}

	rowIndex := 0
	for _, el := range array {
		columnIndex := 0
		for _, char := range el {
			if rowIndex != len(array)-1 {
				tempString := fmt.Sprintf("%c", char)
				num, err := strconv.Atoi(tempString)

				if err != nil {
					fmt.Printf("%s", err)
					os.Exit(1)
				}
				a[rowIndex][columnIndex] = uint8(num)
				columnIndex++
			}
		}
		rowIndex++
	}
	return a
}

func findLeastCommon(arrayA [][]uint8, arrayB [][]uint8) [][]uint8 {
	var array [][]uint8
	if len(arrayA) == 0 || len(arrayB) == 0 {
		if len(arrayA) == 0 {
			array = arrayB
		} else {
			array = arrayA
		}
	} else if len(arrayA) < len(arrayB) {
		array = arrayA
	} else {
		array = arrayB
	}
	return array
}

func findMostCommon(arrayA [][]uint8, arrayB [][]uint8) [][]uint8 {
	var array [][]uint8
	if len(arrayA) >= len(arrayB) {
		array = arrayA
	} else {
		array = arrayB
	}
	return array
}

func getRating(slice [][]uint8, criteria int) int {
	var toIterate [][]uint8
	toIterate = slice

	for i := 0; i < 12; i++ {
		var ones [][]uint8
		var zeros [][]uint8
		for _, v := range toIterate {
			if v[i] == 1 {
				ones = append(ones, v)
			} else {
				zeros = append(zeros, v)
			}
		}

		if criteria == mostCommon {
			toIterate = findMostCommon(ones, zeros)
		} else {
			toIterate = findLeastCommon(ones, zeros)
		}

	}
	return convertArrayToDecimal(toIterate[0])
}

func main() {
	puzzleInput := aocHelper.GetPuzzleInput(3)
	splitInput := strings.Split(puzzleInput, "\n")
	a := convertInputToMatrix(splitInput)
	//Part A
	x := calculatePowerConsumption(a)
	fmt.Println(x)

	//Part B
	oxygenGenRating := getRating(a, mostCommon)
	carbondioxideScrubRating := getRating(a, leastCommon)

	solution := oxygenGenRating * carbondioxideScrubRating

	fmt.Println(solution)

}

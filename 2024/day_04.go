package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	XMAS = "XMAS"
	DIRS = [][2]int{
		{0, 1}, {1, 0}, {0, -1}, {-1, 0}, // Horizontal and vertical
		{1, 1}, {1, -1}, {-1, -1}, {-1, 1}, // Diagonal
	}
)

func readInputAsMatrix(filename string) [][]rune {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var matrix [][]rune
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		matrix = append(matrix, []rune(line))
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}
	return matrix
}

func dfs(matrix [][]rune, i, j, idx, ii, jj int) int {
	if idx == len(XMAS)-1 {
		return 1
	}
	rows, cols := len(matrix), len(matrix[0])
	inext, jnext := i+ii, j+jj
	if inext >= 0 && inext < rows && jnext >= 0 && jnext < cols && matrix[inext][jnext] == rune(XMAS[idx+1]) {
		return dfs(matrix, inext, jnext, idx+1, ii, jj)
	}
	return 0
}

func part1(matrix [][]rune) int {
	result := 0
	rows, cols := len(matrix), len(matrix[0])
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if matrix[i][j] == rune(XMAS[0]) {
				for _, dir := range DIRS {
					ii, jj := dir[0], dir[1]
					if i+ii >= 0 && i+ii < rows && j+jj >= 0 && j+jj < cols {
						result += dfs(matrix, i, j, 0, ii, jj)
					}
				}
			}
		}
	}
	fmt.Println("Part 1:", result)
	return result
}

func part2(matrix [][]rune) int {
	result := 0
	rows, cols := len(matrix), len(matrix[0])
	topleft, bottomright := [2]int{-1, -1}, [2]int{1, 1}
	topright, bottomleft := [2]int{-1, 1}, [2]int{1, -1}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if matrix[i][j] != 'A' {
				continue
			}
			if i-1 < 0 || i+1 >= rows || j-1 < 0 || j+1 >= cols {
				continue
			}
			if !((matrix[i+topleft[0]][j+topleft[1]] == 'M' && matrix[i+bottomright[0]][j+bottomright[1]] == 'S') ||
				(matrix[i+topleft[0]][j+topleft[1]] == 'S' && matrix[i+bottomright[0]][j+bottomright[1]] == 'M')) {
				continue
			}
			if !((matrix[i+topright[0]][j+topright[1]] == 'M' && matrix[i+bottomleft[0]][j+bottomleft[1]] == 'S') ||
				(matrix[i+topright[0]][j+topright[1]] == 'S' && matrix[i+bottomleft[0]][j+bottomleft[1]] == 'M')) {
				continue
			}
			result++
		}
	}
	fmt.Println("Part 2:", result)
	return result
}

func main() {
	filename := "input.txt"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}
	matrix := readInputAsMatrix(filename)
	part1(matrix)
	part2(matrix)
}

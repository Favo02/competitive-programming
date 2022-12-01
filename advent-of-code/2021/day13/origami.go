package main

import (
	"bufio"
	"fmt"
	. "fmt"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	x int
	y int
}

type Fold struct {
	foldNum  int
	foldAxis rune
}

func main() {

	points, folds := parseInput()

	pointsOneFold := fold(points, folds[0].foldNum, folds[0].foldAxis)

	fmt.Println("numero di buchi dopo 1 piega:", len(pointsOneFold))

	for _, f := range folds {
		points = fold(points, f.foldNum, f.foldAxis)
	}

	Println("numero di buchi rimasti dopo le pieghe:", len(points))

	maxX, maxY := max(points)
	printCode(points, maxX, maxY)
}

func fold(points map[Point]bool, foldNum int, foldAxis rune) map[Point]bool {
	for p := range points {
		if foldAxis == 'x' {
			if p.x > foldNum {
				// aggiungo nuovo punto generato dalla piega
				points[Point{foldNum - (p.x - foldNum), p.y}] = true
				// rimuovo punto "vecchio" oltre la piega
				delete(points, p)
			}
		} else {
			if p.y > foldNum {
				// aggiungo nuovo punto generato dalla piega
				points[Point{p.x, foldNum - (p.y - foldNum)}] = true
				// rimuovo punto "vecchio" oltre la piega
				delete(points, p)
			}
		}
	}
	return points
}

func max(points map[Point]bool) (int, int) {
	maxX, maxY := 0, 0
	for p := range points {
		if p.x > maxX {
			maxX = p.x
		}
		if p.y > maxY {
			maxY = p.y
		}
	}
	return maxX, maxY
}

func printCode(points map[Point]bool, maxX, maxY int) {
	for i := 0; i <= maxY; i++ {
		for j := 0; j <= maxX; j++ {
			if _, ok := points[Point{j, i}]; ok {
				Print("#")
			} else {
				Print("-")
			}
		}
		Println()
	}
}

func parseInput() (map[Point]bool, []Fold) {
	paper := make(map[Point]bool, 0)
	folds := make([]Fold, 0)

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, ",") {
			splittedString := strings.Split(line, ",")
			tempCoord := new(Point)
			tempCoord.x, _ = strconv.Atoi(splittedString[0])
			tempCoord.y, _ = strconv.Atoi(splittedString[1])
			paper[*tempCoord] = true
		} else {
			if len(line) != 0 {
				splittedString := strings.Split(line, " ")
				rawFold := strings.Split(splittedString[2], "=")
				axis := []rune(rawFold[0])[0]
				num, _ := strconv.Atoi(rawFold[1])
				fold := Fold{num, axis}
				folds = append(folds, fold)
			}
		}
	}
	return paper, folds
}
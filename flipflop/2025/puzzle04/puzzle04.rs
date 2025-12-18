use itertools::*;
use std::io;
use std::iter;

fn part1(lines: &[(i32, i32)]) -> i32 {
    lines
        .iter()
        .zip(lines.iter().skip(1))
        .map(|((x1, y1), (x2, y2))| (x1 - x2).abs() + (y1 - y2).abs())
        .sum()
}

fn part2(lines: &[(i32, i32)]) -> i32 {
    lines
        .iter()
        .zip(lines.iter().skip(1))
        .map(|((x1, y1), (x2, y2))| (x1 - x2).abs().max((y1 - y2).abs()))
        .sum()
}

fn part3(lines: &[(i32, i32)]) -> i32 {
    let mut lines = lines.to_owned();
    lines.sort_by(|(x1, y1), (x2, y2)| (x1 + y1).cmp(&(x2 + y2)));
    lines
        .iter()
        .zip(lines.iter().skip(1))
        .map(|((x1, y1), (x2, y2))| (x1 - x2).abs().max((y1 - y2).abs()))
        .sum()
}

fn main() {
    let coords: Vec<(i32, i32)> = iter::once((0, 0))
        .chain(io::stdin().lines().map(|l| {
            l.unwrap()
                .split(",")
                .map(|e| e.parse::<i32>().unwrap())
                .collect_tuple()
                .unwrap()
        }))
        .collect();

    println!("Part1: {}", part1(&coords));
    println!("Part2: {}", part2(&coords));
    println!("Part3: {}", part3(&coords));
}

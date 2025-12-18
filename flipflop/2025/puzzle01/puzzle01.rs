use std::*;

fn part1(line: &str) -> i32 {
    line.len() as i32 / 2
}

fn part2(line: &str) -> i32 {
    let sil = part1(line);
    if sil % 2 != 0 { 0 } else { sil }
}

fn part3(line: &str) -> i32 {
    if line.contains('e') {
        0
    } else {
        line.len() as i32 / 2
    }
}

fn main() {
    let lines: Vec<String> = io::stdin().lines().map(|l| l.unwrap()).collect();

    let part1: i32 = lines.iter().map(|line| part1(line)).sum();
    let part2: i32 = lines.iter().map(|line| part2(line)).sum();
    let part3: i32 = lines.iter().map(|line| part3(line)).sum();

    println!("Part1: {}", part1);
    println!("Part2: {}", part2);
    println!("Part3: {}", part3);
}

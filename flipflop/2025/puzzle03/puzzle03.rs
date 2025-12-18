use counter::Counter;
use std::io;

fn part1(lines: &[String]) -> String {
    lines
        .iter()
        .collect::<Counter<_>>()
        .most_common()
        .first()
        .unwrap()
        .0
        .to_string()
}

fn part2(lines: &[String]) -> i32 {
    lines
        .iter()
        .map(|s| {
            s.split(",")
                .map(|e| e.parse::<i32>().unwrap())
                .collect::<Vec<_>>()
        })
        .filter(|el| el[1] > el[0] && el[1] > el[2] && el[0] != el[2])
        .count() as i32
}

fn part3(lines: &[String]) -> i32 {
    lines
        .iter()
        .map(|s| {
            s.split(",")
                .map(|e| e.parse::<i32>().unwrap())
                .collect::<Vec<_>>()
        })
        .map(|el| {
            let (r, g, b) = (el[0], el[1], el[2]);
            match (r, g, b) {
                (r, g, b) if r == g || g == b || r == b => 10,
                (r, g, b) if r > g && r > b => 5,
                (r, g, b) if g > r && g > b => 2,
                (r, g, b) if b > r && b > g => 4,
                _ => panic!("{} {} {}", r, g, b),
            }
        })
        .sum()
}

fn main() {
    let lines: Vec<String> = io::stdin().lines().map(|l| l.unwrap()).collect();

    println!("Part1: {}", part1(&lines));
    println!("Part2: {}", part2(&lines));
    println!("Part3: {}", part3(&lines));
}

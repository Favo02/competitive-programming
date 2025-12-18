use itertools::*;
use std::io;

const SKY: i64 = 1000;
const PHOTO: i64 = 500;
const AREA: (i64, i64) = ((SKY - PHOTO) / 2, (SKY - PHOTO) / 2 + (SKY - PHOTO));

fn simulate(birds: Vec<(i64, i64)>, speeds: &[(i64, i64)], seconds: i64) -> Vec<(i64, i64)> {
    birds
        .iter()
        .zip(speeds.iter())
        .map(|((x, y), (sx, sy))| {
            (
                (x + sx * seconds).rem_euclid(SKY),
                (y + sy * seconds).rem_euclid(SKY),
            )
        })
        .collect()
}

fn count(birds: &Vec<(i64, i64)>) -> i64 {
    birds
        .iter()
        .filter(|(x, y)| *x >= AREA.0 && *x < AREA.1 && *y >= AREA.0 && *y < AREA.1)
        .count() as i64
}

fn part1(speeds: &[(i64, i64)]) -> i64 {
    const SECONDS: i64 = 100;

    count(&simulate(
        (0..speeds.len()).map(|_| (0, 0)).collect(),
        speeds,
        SECONDS,
    ))
}

fn part2(speeds: &[(i64, i64)]) -> i64 {
    const ROUNDS: i64 = 1000;
    const SECONDS: i64 = 3600;

    let mut birds: Vec<(i64, i64)> = (0..speeds.len()).map(|_| (0, 0)).collect();
    let mut res = 0;

    for _ in 0..ROUNDS {
        birds = simulate(birds, speeds, SECONDS);
        res += count(&birds);
    }
    res
}

fn part3(speeds: &[(i64, i64)]) -> i64 {
    const ROUNDS: i64 = 1000;
    const SECONDS: i64 = 31556926;

    let mut birds: Vec<(i64, i64)> = (0..speeds.len()).map(|_| (0, 0)).collect();
    let mut res = 0;

    for _ in 0..ROUNDS {
        birds = simulate(birds, speeds, SECONDS);
        res += count(&birds);
    }
    res
}

fn main() {
    let speeds: Vec<(i64, i64)> = io::stdin()
        .lines()
        .map(|l| {
            l.unwrap()
                .split(",")
                .map(|e| e.parse::<i64>().unwrap())
                .collect_tuple()
                .unwrap()
        })
        .collect();

    println!("Part1: {}", part1(&speeds));
    println!("Part2: {}", part2(&speeds));
    println!("Part3: {}", part3(&speeds));
}

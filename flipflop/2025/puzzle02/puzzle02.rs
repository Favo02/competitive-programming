use memoize::memoize;
use std::*;

fn part1(moves: &[i32]) -> i32 {
    moves
        .iter()
        .fold((0, 0), |(sum, mx), &e| (sum + e, mx.max(sum + e)))
        .1
}

fn part2(moves: &[i32]) -> i32 {
    let mut last: Option<i32> = None;
    let mut cur = 0;
    let mut res = 0;
    for &m in moves {
        last = match last {
            Some(n) if n > 0 && m > 0 => Some(n + 1),
            Some(n) if n < 0 && m < 0 => Some(n - 1),
            _ => Some(m),
        };
        cur += last.unwrap();
        res = res.max(cur);
    }
    res
}

fn part3(moves: &[i32]) -> i32 {
    #[memoize]
    fn fib(n: i32) -> i32 {
        match n {
            1 | 2 => 1,
            _ => fib(n - 1) + fib(n - 2),
        }
    }

    let mut last: Option<i32> = None;
    let mut cur = 0;
    let mut res = 0;
    for (i, &m) in moves.iter().enumerate() {
        last = match last {
            Some(n) if i != moves.len() - 1 && n > 0 && m > 0 => Some(n + 1),
            Some(n) if i != moves.len() - 1 && n < 0 && m < 0 => Some(n - 1),
            None => Some(m),
            _ => {
                let n = last.unwrap();
                if n > 0 {
                    cur += fib(n);
                } else {
                    cur -= fib(n.abs());
                }
                res = res.max(cur);
                Some(m)
            }
        };
    }
    res
}

fn main() {
    let line: String = io::stdin().lines().next().unwrap().unwrap();
    let moves: Vec<i32> = line
        .chars()
        .map(|c| match c {
            '^' => 1,
            'v' => -1,
            _ => panic!(),
        })
        .collect();

    println!("Part1: {}", part1(&moves));
    println!("Part2: {}", part2(&moves));
    println!("Part3: {}", part3(&moves));
}

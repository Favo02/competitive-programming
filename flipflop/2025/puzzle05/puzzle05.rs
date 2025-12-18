use itertools::*;
use std::collections::{HashMap, HashSet};
use std::io;

fn visit(map: &String) -> Vec<(char, i32)> {
    let mut tunnels: HashMap<char, (usize, usize)> = HashMap::new();
    for (i, c) in map.chars().enumerate() {
        if tunnels.contains_key(&c) {
            tunnels.insert(c, (tunnels.get(&c).unwrap().0, i));
        } else {
            tunnels.insert(c, (i, 0));
        }
    }

    let map: Vec<char> = map.chars().collect();

    let mut cur: usize = 0;
    let mut visited = Vec::new();

    while cur < map.len() {
        let dist = tunnels.get(&map[cur]).unwrap();
        visited.push((map[cur], (dist.0 as i32 - dist.1 as i32).abs()));
        let (a, b) = tunnels.get(&map[cur]).unwrap();
        let next = if *a == cur { *b } else { *a };
        cur = next + 1;
    }

    visited
}

fn part1(visited: &Vec<(char, i32)>) -> i32 {
    visited.iter().map(|(_, d)| d).sum()
}

fn part2(map: &String, visited: &Vec<(char, i32)>) -> String {
    let visited: HashSet<char> = HashSet::from_iter(visited.iter().map(|(c, _d)| *c));
    map.chars()
        .filter(|c| !visited.contains(c))
        .unique()
        .collect::<String>()
}

fn part3(visited: &Vec<(char, i32)>) -> i32 {
    visited
        .iter()
        .map(|(c, d)| if c.is_lowercase() { *d } else { -d })
        .sum()
}

fn main() {
    let line: String = io::stdin().lines().next().unwrap().unwrap();

    let visited = visit(&line);

    println!("Part1: {}", part1(&visited));
    println!("Part2: {}", part2(&line, &visited));
    println!("Part3: {}", part3(&visited));
}

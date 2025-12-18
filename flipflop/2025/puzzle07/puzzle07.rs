use itertools::*;
use std::{
    collections::{HashMap, HashSet, VecDeque},
    io,
};

fn part1(sizes: &Vec<(i64, i64)>) -> i64 {
    let grids: Vec<Vec<Vec<i64>>> = sizes
        .iter()
        .map(|(r, c)| (0..*r).map(|_| (0..*c).map(|_| 0).collect()).collect())
        .collect();

    let mut res = 0;
    for mut grid in grids {
        for y in 0..grid.len() {
            for x in 0..grid[0].len() {
                if y == 0 && x == 0 {
                    grid[0][0] = 1;
                } else if y == 0 {
                    grid[0][x] = grid[0][x - 1];
                } else if x == 0 {
                    grid[y][0] = grid[y - 1][0];
                } else {
                    grid[y][x] = grid[y - 1][x] + grid[y][x - 1];
                }
            }
        }
        res += grid.last().unwrap().last().unwrap();
    }
    res
}

fn part2(sizes: &Vec<(i64, i64)>) -> i64 {
    let grids: Vec<Vec<Vec<Vec<i64>>>> = sizes
        .iter()
        .map(|(xz, y)| {
            (0..*xz)
                .map(|_| (0..*y).map(|_| (0..*xz).map(|_| 0).collect()).collect())
                .collect()
        })
        .collect();

    let mut res = 0;
    for mut grid in grids {
        for z in 0..grid.len() {
            for y in 0..grid[0].len() {
                for x in 0..grid[0][0].len() {
                    if z == y && y == x && x == 0 {
                        grid[z][y][x] = 1;
                        continue;
                    }

                    let zz = match grid.get(z - 1) {
                        Some(g) => g[y][x],
                        None => 0,
                    };
                    let yy = match grid[z].get(y - 1) {
                        Some(g) => g[x],
                        None => 0,
                    };
                    let xx = match grid[z][y].get(x - 1) {
                        Some(g) => *g,
                        None => 0,
                    };

                    grid[z][y][x] = zz + yy + xx;
                }
            }
        }
        res += grid.last().unwrap().last().unwrap().last().unwrap();
    }
    res
}

fn part3(sizes: &Vec<(i64, i64)>) -> i64 {
    let mut res = 0;
    for (dims, size) in sizes {
        let mut grid = HashMap::new();
        let mut queue = VecDeque::new();
        let mut seen = HashSet::new();

        grid.insert((0..*dims).map(|_| 0).collect::<Vec<_>>(), 1);
        queue.push_back((0..*dims).map(|_| 0).collect::<Vec<_>>());

        while let Some(cur) = queue.pop_front() {
            let mut next = cur.clone();
            for (i, n) in cur.iter().enumerate() {
                if *n < size - 1 {
                    next[i] += 1;

                    *grid.entry(next.to_owned()).or_insert(0) += grid[&cur];

                    if let None = seen.get(&next) {
                        queue.push_back(next.clone());
                        seen.insert(next.clone());
                    }

                    next[i] -= 1;
                }
            }
        }

        res += grid
            .get(&(0..*dims).map(|_| size - 1).collect::<Vec<_>>())
            .unwrap();
    }
    res
}

fn main() {
    let sizes: Vec<(i64, i64)> = io::stdin()
        .lines()
        .map(|l| {
            l.unwrap()
                .split(" ")
                .map(|e| e.parse::<i64>().unwrap())
                .collect_tuple()
                .unwrap()
        })
        .collect();

    println!("Part1: {}", part1(&sizes));
    println!("Part2: {}", part2(&sizes));
    println!("Part3: {}", part3(&sizes));
}

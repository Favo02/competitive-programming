use std::{
    collections::HashMap,
    io::{self, BufRead},
};

fn main() {
    let parsed: Vec<(i32, Vec<i32>)> = io::stdin()
        .lock()
        .lines()
        .map(|l| l.unwrap())
        .map(|line| {
            let (id, rest) = line.split_once(':').unwrap();
            let values: Vec<_> = rest
                .split_whitespace()
                .map(|w| {
                    w.chars()
                        .map(|c| if c.is_lowercase() { '0' } else { '1' })
                        .collect::<String>()
                })
                .map(|s| i32::from_str_radix(&s, 2).unwrap())
                .collect();
            (id.parse::<i32>().unwrap(), values)
        })
        .collect();

    #[derive(Debug, Eq, Hash, PartialEq)]
    enum SCALE {
        MATTE,
        SHINY,
    }
    #[derive(Debug, Eq, Hash, PartialEq)]
    enum COLOR {
        RED,
        GREEN,
        BLUE,
    }

    let mut counter: HashMap<(SCALE, COLOR), (i32, i32)> = HashMap::new();

    parsed
        .iter()
        .map(|(id, values)| {
            let s = match values[3] {
                0..=30 => Some(SCALE::MATTE),
                33..=64 => Some(SCALE::SHINY),
                _ => None,
            };
            let c = if values[0] > values[1] && values[0] > values[2] {
                Some(COLOR::RED)
            } else if values[1] > values[0] && values[1] > values[2] {
                Some(COLOR::GREEN)
            } else if values[2] > values[0] && values[2] > values[1] {
                Some(COLOR::BLUE)
            } else {
                None
            };
            (id, s, c)
        })
        .filter(|(_, scale, color)| scale.is_some() && color.is_some())
        .for_each(|(id, scale, color)| {
            let entry = counter
                .entry((scale.unwrap(), color.unwrap()))
                .or_insert((0, 0));
            entry.0 += 1;
            entry.1 += id;
        });

    let res = counter.values().max_by_key(|(count, _)| count).unwrap().1;

    println!("{}", res);
}

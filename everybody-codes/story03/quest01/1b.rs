use std::io::{self, BufRead};

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

    let max_shine = parsed.iter().map(|(_, values)| values[3]).max().unwrap();

    let res = parsed
        .iter()
        .filter(|(_, values)| values[3] == max_shine)
        .min_by_key(|(_, values)| values[0..3].iter().sum::<i32>())
        .unwrap()
        .0;

    println!("{:?}", res);
}

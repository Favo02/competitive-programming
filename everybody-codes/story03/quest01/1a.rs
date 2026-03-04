use std::io::{self, BufRead};

fn main() {
    let res: i32 = io::stdin()
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
        .filter(|(_, values)| values[1] > values[0] && values[1] > values[2])
        .map(|(id, _)| id)
        .sum();

    println!("{}", res);
}

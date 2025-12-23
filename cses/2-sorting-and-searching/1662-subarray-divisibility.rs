use std::{collections::HashMap, *};

fn main() {
    let lines: Vec<String> = io::stdin().lines().map(|l| l.unwrap()).collect();

    let n = lines[0].parse::<i64>().unwrap();
    let nums = lines[1]
        .split(' ')
        .map(str::parse::<i64>)
        .map(result::Result::unwrap)
        .collect::<Vec<i64>>();

    assert_eq!(n, nums.len() as i64);

    let mut seen: HashMap<i64, i64> = HashMap::new();
    seen.insert(0, 1);
    let mut sum = 0;

    let mut res = 0;

    for x in &nums {
        sum += x;
        let target = sum.rem_euclid(n);
        if let Some(qty) = seen.get(&target) {
            res += qty;
        }
        *seen.entry(target).or_insert(0) += 1;
    }

    println!("{}", res);
}

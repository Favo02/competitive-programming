use std::{collections::HashMap, *};

fn main() {
    let lines: Vec<String> = io::stdin().lines().map(|l| l.unwrap()).collect();

    let [n, x] = lines[0]
        .split(' ')
        .map(str::parse::<i64>)
        .map(result::Result::unwrap)
        .collect::<Vec<i64>>()
        .try_into()
        .unwrap();

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

    for n in &nums {
        sum += n;
        if let Some(qty) = seen.get(&(sum - x)) {
            res += qty;
        }
        *seen.entry(sum).or_insert(0) += 1;
    }

    println!("{}", res);
}

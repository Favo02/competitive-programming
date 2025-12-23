use std::*;

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

    let mut start = 0;
    let mut sum = 0;
    let mut res = 0;

    for end in 0..n {
        sum += nums[end as usize];
        while sum > x && start < end {
            sum -= nums[start as usize];
            start += 1;
        }
        if sum == x {
            res += 1;
        }
    }

    println!("{}", res);
}

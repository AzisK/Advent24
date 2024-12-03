use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_input(file_path: &str) -> io::Result<impl Iterator<Item = String>> {
    let path = Path::new(file_path);
    let file = File::open(&path)?;
    let reader = io::BufReader::new(file);
    Ok(reader.lines().filter_map(Result::ok))
}

fn process_input(file_path: &str) -> (Vec<i32>, Vec<i32>) {
    let lines = read_input(file_path).expect("Failed to read input file");
    let mut left = Vec::new();
    let mut right = Vec::new();

    for line in lines {
        let numbers: Vec<i32> = line.split_whitespace()
                                    .map(|s| s.parse().unwrap())
                                    .collect();
        if numbers.len() == 2 {
            left.push(numbers[0]);
            right.push(numbers[1]);
        }
    }

    left.sort();
    right.sort();

    (left, right)
}

fn main() {
    let (left, right) = process_input("Input/1.txt");

    // Good to see //
    println!("Left\tRight\tDifference");
    for (l, r) in left.iter().zip(right.iter()) {
        println!("{}\t{}\t{}", l, r, (l - r).abs());
    }
    // Good to see //

    let answer: i32 = left.iter().zip(right.iter()).map(|(l, r)| (l - r).abs()).sum();
    println!("Answer: {}", answer);
}
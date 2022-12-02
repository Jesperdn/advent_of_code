use utils::read_lines;
use std::collections::BinaryHeap;

fn part_one(file: &str) -> i32 {
    let mut highest: i32 = 0;
    let mut calories: i32 = 0;
    if let Ok(lines) = read_lines(file) {
        for line in lines {
            if let Ok(ln) = line {
                if ln.eq("") {
                    highest = if calories>highest {calories} else {highest};
                    calories = 0;
                } else {
                    calories+=ln.parse::<i32>().unwrap();
                }
            }
        }
    }
    return highest
}

fn part_two(file: &str) -> i32 {
    let mut elves = BinaryHeap::new();
    let mut calories: i32 = 0;
    if let Ok(lines) = read_lines(file) {
        for line in lines {
            if let Ok(ln) = line {
                if ln.eq("") {
                    elves.push(calories);
                    calories = 0;
                } else {
                    calories+=ln.parse::<i32>().unwrap();
                }
            }
        }
    }
    let mut top_three = 0;
    for _ in 0..3 {
        top_three += elves.pop().unwrap();
    }
    return top_three;
}

fn main() {
    println!("{}", part_one("input"));
    println!("{}", part_two("input"));
}

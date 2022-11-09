use std::fs::File;
use std::io::{BufReader, BufRead, Error};
use std::fs;


fn is_nice(string: &str) -> bool {
    let vowels = vec!['a','e','i','o','u'];
    let mut vowel_count = 0;
    let mut double = false;

    for i in 1..(string.len()-1) {
        println!("{} : {}", i, string[i])
    }

    for (i, c) in string.chars().enumerate() {
        println!("{} : {}", i, c);
    }


    return true;
}

fn part_one(file: &str) {
    let mut nice_strings = 0;

    let input = File::open(&file)
        .expect("Could not open file\n");
    let buffered = BufReader::new(input);

    for line in buffered.lines() {
        match line {
            Ok(str) => nice_strings+= if is_nice(&str) {1} else {0},
            Err(_) => continue,
        }

        //println!("{:?}", line);
    }
}   


fn part_two(file: &str) {

}


fn main() {
    println!("Hello, world!");
    part_one("src/test.in");

}

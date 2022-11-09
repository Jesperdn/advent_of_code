use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, { 
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}



fn part_one(file: &str) -> i32 {
    let mut total = 0;

    if let Ok(lines) = read_lines(file) {
        for line in lines {
            if let Ok(ln) = line {
                println!("{}",ln);
                // Split and map to integers
                let mut split = ln.trim().split("x");

                let lwh: Vec<i32> = split
                    .map(|x| x.parse::<i32>().unwrap())
                    .collect();
                println!("{} {} {}", lwh[0], lwh[1], lwh[2]);
                

                // Create a Vec with the calculated side values
                let s: Vec<i32> = lwh
                    .iter()
                    .enumerate()
                    .map(|(i, &x)| x * (lwh[(i+1)%3]))
                    .collect();
                println!("{} {} {}", s[0], s[1], s[2]);

                // Calculate present paper
                //let ssum: i32 = s.iter().sum().unwrap();
                let min = s.iter().min().unwrap();
                let ssum: i32 = s.iter().fold(0, |acc, x| acc + 2*x);
                println!("{}, {}", ssum, min);
                total += ssum + min;
            }
        }
    }   
    return total;
}

fn main() {
    println!("Hello, world!");
    println!("{}", part_one("input"));

}

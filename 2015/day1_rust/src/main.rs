use std::fs;

fn part_one(file: &str) -> i32 {
    let mut floor = 0;

    let contents = fs::read_to_string(file)
        .expect("Could not open file");
    
    for c in contents.chars() {
        match c {
            '(' => floor+=1,
            ')' => floor-=1,
            _ => continue,
        }
    }
    return floor;
}

fn part_two(file: &str) -> i32 {
    let mut floor = 0;

    let contents = fs::read_to_string(file)
        .expect("error");
    
    for (i, c) in contents.chars().enumerate() {
        match c {
            '(' => floor+=1,
            ')' => floor-=1,
            _ => continue,
        
        }
        if floor < 0 {
            return (i+1).try_into().unwrap();
        }
    }
    return -1;
}


fn main() {
    println!("{}", part_one("input"));
    println!("{}", part_two("input"));
}

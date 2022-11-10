use utils::read_lines;
use std::collections::HashSet;

fn part_one(file: &str) -> i32 {
    let mut x = 0;
    let mut y = 0;
    let mut known: HashSet<(i32, i32)> = HashSet::new();
    known.insert((x,y));
        
    if let Ok(lines) = read_lines(file) {
        for line in lines {
            if let Ok(ln) = line {
                for c in ln.chars() {
                    match c {
                        '^' => y+=1,
                        'v' => y-=1,
                        '>' => x+=1,
                        '<' => x-=1,
                        _ => continue,
                    }
                    known.insert((x,y));
                }
            }
        }
    }
    return known.len() as i32;
}

fn part_two(file: &str) -> i32 {
    let (mut sx, mut sy, mut rx, mut ry) = (0,0,0,0);
    let mut known: HashSet<(i32, i32)> = HashSet::new();
    known.insert((sx,sy));

    if let Ok(lines) = read_lines(file) {
        for line in lines {
            if let Ok(ln) = line {
                for (i, c) in ln.chars().enumerate() {
                    match c {
                        '^' => if i%2==0 {ry+=1} else {sy+=1},
                        'v' => if i%2==0 {ry-=1} else {sy-=1},
                        '>' => if i%2==0 {rx+=1} else {sx+=1},
                        '<' => if i%2==0 {rx-=1} else {sx-=1},
                        _ => continue,
                    }
                    known.insert((sx,sy));
                    known.insert((rx,ry));
                }
            }
        }
    }
    return known.len() as i32
}

fn main() {
    println!("{}", part_one("input"));
    println!("{}", part_two("input"));
}

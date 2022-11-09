import sys
import numpy as np

def calc_lights(x1: int, y1: int, x2: int, y2: int):
    return (x2-x1+1)*(y2-y1+1)

def part_one(input: str) -> int:    

    grid = np.empty([1000,1000])
    print(grid)

    total: int = 0
    with open(input, 'r') as inp:
        for line in inp:
            splt = line.split()
            if splt[0] == "toggle":
                ...
            elif splt[1] == "on":
                ...
            print(splt)


def part_two(input: str) -> int:
    ...
    with open(input, 'r') as inp:
        ...

def main():
    print(part_one(sys.argv[1]))
    print(part_two(sys.argv[1]))

if __name__=="__main__":
    main()
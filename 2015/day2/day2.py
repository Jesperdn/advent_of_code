from math import prod
import sys


def part_one(input : str) -> int:
    total : int = 0
    with open(input, 'r') as inp:
        for i, line in enumerate(inp):
            l,w,h = line.split("x")
            s1 = int(l)*int(w)
            s2 = int(w)*int(h)
            s3 = int(h)*int(l)
            smallest = min(s1,s2,s3)
            total += 2*s1 + 2*s2 + 2*s3 + smallest
    return total


def part_two(input : str) -> int:
    total : int = 0
    with open(input, 'r') as inp:
        for i, line in enumerate(inp):
            lwh = [int(x) for x in line.split("x")]
            cubic_feet = prod(lwh)
            smallest = lwh.pop(lwh.index(min(lwh)))
            next_sml = lwh.pop(lwh.index(min(lwh)))
            total += (smallest*2 + next_sml*2) + cubic_feet
    return total



def main() -> None:
    print("Wrapping paper needed:", part_one(sys.argv[1]))
    print("Ribbon needed:", part_two(sys.argv[1]))



if __name__=="__main__":
    main()
    
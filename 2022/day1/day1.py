import sys

def part_one(input: str) -> int:
    with open(input, 'r') as inp:
        total = 0
        for line in inp.readlines():
            if line.strip():
                total+=int(line)
            else:
                highest = total if total>highest else highest
                total = 0
    return highest
        

def part_two(input: str) -> int:
    elves = list()
    with open(input, 'r') as inp:
        total = 0
        for line in inp.readlines():
            if line.strip():
                total+=int(line)
            else:
                elves.append(total)
                total = 0
    elves.sort(reverse=True)
    return elves[0]+elves[1]+elves[2]

def main():
    print(part_one(sys.argv[1]))
    print(part_two(sys.argv[1]))

if __name__=="__main__":
    main()
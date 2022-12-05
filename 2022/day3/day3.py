import sys

def part_one(input: str) -> int:
    total_pri = 0
    with open(input, 'r') as inp:
        for line in inp:
            common = ''.join(set(line[0:len(line)//2]).intersection(set(line[len(line)//2:])))
            total_pri += ord(common)-38 if common.isupper() else ord(common)-96
    return total_pri

def part_two(input: str) -> int:
    total_pri = 0
    with open(input, 'r') as inp:
        lines = inp.readlines()
        for i in range(0, len(lines), 3):
            common = ''.join(set(lines[i]) & set(lines[i+1]) & set(lines[i+2])).strip()
            total_pri += ord(common)-38 if common.isupper() else ord(common)-96
    return total_pri
            
        


def main():
    print(part_one(sys.argv[1]))
    print(part_two(sys.argv[1]))

if __name__=="__main__":
    main()
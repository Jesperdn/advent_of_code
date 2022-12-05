import sys

def part_one(input: str) -> int:
    overlaps = 0
    with open(input, 'r') as inp:
        for line in inp:
            sec1, sec2 = [list(map(int, x)) for x in [sec.split("-") for sec in line.strip().split(",")]]
            if (sec1[0]<=sec2[0] and sec1[1]>=sec2[1]) or (sec1[0]>=sec2[0] and sec1[1]<=sec2[1]):
                overlaps+=1
    return overlaps
            
def part_two(input: str) -> int:
    overlaps = 0
    with open(input, 'r') as inp:
        for line in inp:
            sec1, sec2 = [list(map(int, x)) for x in [sec.split("-") for sec in line.strip().split(",")]]
            if len(set(list(range(sec1[0], sec1[1]+1))).intersection(set(list(range(sec2[0], sec2[1]+1))))):
                overlaps+=1
    return overlaps

def main():
    print(part_one(sys.argv[1]))
    print(part_two(sys.argv[1]))

if __name__=="__main__":
    main()
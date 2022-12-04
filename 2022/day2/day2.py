import sys

def part_one(input: str) -> int:
    scores = {'Y':2, 'X':1, 'Z':3}
    wins=[['A','Y'],['B','Z'],['C','X']]
    equals=[['A','X'],['B','Y'],['C','Z']]
    score = 0
    with open(input, 'r') as inp:
        for line in inp.readlines():
            strat = line.split()
            score += 6 if strat in wins else 3 if strat in equals else 0
            score += scores[strat[1]]
    return score

def part_two(input: str) -> int:
    loss={'B':1,'A':3,'C':2}
    wins={'A':2,'B':3,'C':1}
    draw={'A':1,'B':2,'C':3}
    score = 0
    with open(input, 'r') as inp:
        for line in inp.readlines():
            p,strat = line.split()
            if strat=='Z':
                score+=wins[p] + 6
            elif strat=='Y':
                score+=draw[p] + 3
            else: score += loss[p]
    return score


def main():
    print(part_one(sys.argv[1]))
    print(part_two(sys.argv[1]))

if __name__=="__main__":
    main()
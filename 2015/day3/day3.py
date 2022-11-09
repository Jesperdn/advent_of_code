import sys

def part_one(input: str) -> int:
    pos_x : int = 0
    pos_y : int = 0
    known : set = set()    
    known.add((pos_x, pos_y))

    with open(input, 'r') as inp:
        moves = inp.readline()
        for char in moves:
            if char=='^':
                pos_y+=1
            if char=='v':
                pos_y-=1
            if char=='>':
                pos_x+=1
            if char=='<':
                pos_x-=1
            known.add((pos_x, pos_y))
    return len(known)

def part_two(input: str) -> int:
    r_pos_x : int = 0
    r_pos_y : int = 0
    s_pos_x : int = 0
    s_pos_y : int = 0
    known : set = set()
    known.add((r_pos_x, r_pos_y))

    with open(input, 'r') as inp:
        moves = inp.readline()
        for i, char in enumerate(moves):
            if char=='^':
                if (i%2==0): r_pos_y+=1 
                else: s_pos_y+=1
            if char=='v':
                if (i%2==0): r_pos_y-=1 
                else: s_pos_y-=1
            if char=='>':
                if (i%2==0): r_pos_x+=1 
                else: s_pos_x+=1
            if char=='<':
                if (i%2==0): r_pos_x-=1 
                else: s_pos_x-=1
            known.add((r_pos_x, r_pos_y))
            known.add((s_pos_x, s_pos_y))
    return len(known)
            
            

def main():
    print(part_one(sys.argv[1]))
    print(part_two(sys.argv[1]))

if __name__=="__main__":
    main()
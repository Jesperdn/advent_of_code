import sys
import hashlib

def part_one(input: str) -> int:
    with open(input, 'r') as inp:
        key : str = inp.readline()
        for i in range(10000000):
            hash = hashlib.md5((key + str(i)).encode()).hexdigest()
            if hash[:5]=="00000":
                return i       
    



def part_two(input: str) -> int:
    with open(input, 'r') as inp:
        key : str = inp.readline()
        for i in range(10000000):
            hash = hashlib.md5((key + str(i)).encode()).hexdigest()
            if hash[:6]=="000000":
                return i    

def main():
    print(part_one(sys.argv[1]))
    print(part_two(sys.argv[1]))

if __name__=="__main__":
    main()
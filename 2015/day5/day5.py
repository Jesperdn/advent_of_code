import sys

def is_nice(string: str) -> bool:
    vowels: str = "aeiou"
    vowel_count: int = 0
    double: bool = False
    bad_chars: list = ["ab", "cd", "pq", "xy"]

    for i, char in enumerate(string):
        vowel_count += 1 if char in vowels else 0
        if i+1 < len(string):
            double = string[i+1]==char if double==False else double
            if char + string[i+1] in bad_chars:
                return False
    return double and (vowel_count>=3)


def is_nice_2(string: str) -> bool:
    pairs: int = 0
    repeats: int = 0
    n = len(string)
    

    for i in range(0, n-1):
        pair = string[i]+string[i+1]
        pairs += 1 if pair in string[i+2:] else 0
    for i in range(0, n-2):
        repeats += 1 if string[i] == string[i+2] else 0

    return (pairs != 0) and (repeats != 0)



def part_one(input: str) -> int:
    nice_strings : int = 0
    with open(input, 'r') as inp:
        for line in inp:
            nice_strings += 1 if is_nice(line) else 0
    return nice_strings


def part_two(input: str) -> int:
    nice_strings: int = 0
    
    with open(input, 'r') as inp:
        for line in inp:
            nice_strings += 1 if is_nice_2(line) else 0
    return nice_strings


def main():
    print(part_one(sys.argv[1]))
    print(part_two(sys.argv[1]))

if __name__=="__main__":
    main()
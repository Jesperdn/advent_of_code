floor : int = 0
basement : int = 0
with open("input", "r") as input:
    for i, char in enumerate(input.readline()):
        floor += 1 if char=='(' else -1
        if floor < 0:
            basement = i+1
            break
print(floor)
print(basement)

# Turns nums, returns new value of i
def turn_dial(i: int, dir: str, val: int, R: int) -> int:
    if dir == "R":
        while (i + val) > R:
            # Calculate excess, reset back to 0
            val -= (R - i)+1
            i = 0
        return i + val

    else:
        while (i - val) < 0: 
            # Calculate excess, reset back to R
            val -= i + 1
            i = R

        return i - val

def calculate_password(rotations: list[str], i: int = 0) -> int:
    nums: list[int] = [i for i in range(100)]
    res: int = 0
    i = i

    for line in rotations:
        # remove newline
        line = line.strip()
        dir = line[0:1]
        val = int(line[1:])

        i = turn_dial(i, dir, val, len(nums)-1)

        if i == 0:
            res += 1

    return res


def day_1(input_path:str = "src/day_1/input.txt"):
    rotations = []
    with open(input_path, "r") as f:
        rotations = f.readlines()

    print(calculate_password(rotations, 50))

if __name__ == "__main__":
    #print(turn_dial(82, "L", 30, 99))
    print(calculate_password([
        "R50",
        "L68", 
        "L30", 
        "R48", 
        "L5", 
        "R60", 
        "L55", 
        "L1", 
        "L99", 
        "R14", 
        "L82", 
    ], 0))

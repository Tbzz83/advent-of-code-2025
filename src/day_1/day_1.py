def turn_dial_2(i: int, dir: str, val: int, R: int) -> tuple[int, int]:
    zeros = 0
    if dir == "R":
        while (i + val) > R:
            # Calculate excess, reset back to 0
            val -= (R - i)+1
            i = 0
            zeros += 1
        i = i + val
        if i == 0 and val > 0:
            zeros += 1

        return (i, zeros)

    while (i - val) < 0: 
        # Calculate excess, reset back to R
        val -= i + 1

        # Don't increment if i was already sitting at 0
        zeros += 1 if i > 0 else 0
        i = R

    i = i - val

    if i == 0 and val > 0:
        zeros += 1

    return (i, zeros)

# Turns nums, returns new value of i
def turn_dial(i: int, dir: str, val: int, R: int) -> int:
    if dir == "R":
        while (i + val) > R:
            # Calculate excess, reset back to 0
            val -= (R - i)+1
            i = 0
        return i + val

    while (i - val) < 0: 
        # Calculate excess, reset back to R
        val -= i + 1
        i = R

    return i - val

def calculate_password_2(rotations: list[str], i: int = 0) -> int:
    nums: list[int] = [i for i in range(100)]
    res: int = 0
    i = i

    for line in rotations:
        # remove newline
        line = line.strip()
        dir = line[0:1]
        val = int(line[1:])

        (i, zeros) = turn_dial_2(i, dir, val, len(nums)-1)

        res += zeros

    return res

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

    print("calculate password part 1")
    print(calculate_password(rotations, 50))

    print("\ncalculate password part 2")
    print(calculate_password_2(rotations, 50))

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
    ], 50))

    print(calculate_password_2([
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
    ], 50))

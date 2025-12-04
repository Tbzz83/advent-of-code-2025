# DP solution
def get_joltage_2_optimized(str_num: str, batteries=12) -> int:

    # first val is index, second is value
    res = ""

    cur: list[int] = [0,0]
    while True:

        if batteries == 0:
            break

        #print(f"next_i {next_i}, cur: {cur}")
        #for idx, num in enumerate(str_num[cur[0]:len(str_num)-batteries+1]):
        idx = cur[0]
        while idx != len(str_num)-batteries+1:
            num_i = int(str_num[idx])
            if num_i > cur[1]:
                #print(f"idx {idx} num_i {num_i} cur: {cur}")
                cur[0], cur[1] = idx, num_i

            idx += 1

        res += str(cur[1])
        batteries -= 1
        cur[0] += 1
        cur[1] = 0

    return int(res)

# DP solution
# This one is currently broken idk why
def get_joltage_2(str_num: str, batteries=12) -> int:

    cache: dict[tuple[int, int], str] = {}

    def dp(i: int, needs_len: int) -> str:
        key = (i, needs_len)
        if i >= len(str_num) and needs_len != 0:
            return str(0)

        if needs_len == 1:
            cache[key] = str_num[i]
            return str_num[i]


        if key in cache:
            return cache[key]

        if i == len(str_num) - 1:
            cache[key] = str(0)
            return cache[key]

        pick, skip = str_num[i] + dp(i+1, needs_len - 1), dp(i+1, needs_len)

        cache[key] = str(max(int(pick), int(skip)))
        return cache[key]

    

    res = int(dp(0, batteries))
    #print(cache)
    return res

# Inefficient
def get_joltage_2_backtrack(str_num: str, batteries=12) -> int:
    res = [0]

    def backtrack(i: int, substr: str):
        if len(substr) > 0:
            if int(substr[0]) < int(str(res[0])[0]):
                return

        if len(substr) == batteries:
            res[0] = max(res[0], int(substr))

        if i-1 + (batteries - len(substr)) >= len(str_num):
            return
        if i >= len(str_num):
            return
        
        #print(f"i: {i}, substr: {substr}")
        # pick
        backtrack(i+1, substr+str_num[i])

        # skip
        backtrack(i+1, substr)

    backtrack(0, "")

    return res[0]


def get_joltage_1(str_num: str) -> int:
    res = 0
    l_max, r_max = 0,0

    for i, n in enumerate(str_num):
        #print(f"i: {i} n: {n} lmax: {l_max} rmax: {r_max}")
        int_n = int(n)
        if int_n > l_max and i != len(str_num) - 1:
            l_max = int_n
            r_max = int(str_num[i+1])

        else:
            r_max = max(r_max, int_n)

        res = max(res, int(str(l_max) + str(r_max)))

    return res

def part_2(nums: list[str]) -> int:

    res: int  = 0

    for str_num in nums:
        joltage = get_joltage_2(str_num)
#        print(f"num {str_num} has joltage {joltage}")

        res += joltage

    return res

def part_1(nums: list[str]) -> int:

    res: int  = 0

    for str_num in nums:
        joltage = get_joltage_1(str_num)
        print(f"num {str_num} has joltage {joltage}")

        res += joltage

    return res

def day_3():
    with open("src/day_3/input.txt", "r") as f:
        nums = list(map(lambda x: x.strip(), f.readlines()))

#    nums = [
#        "987654321111111",
#        "811111111111119",
#        "234234234234278",
#        "818181911112111",
#    ]

    print(part_2(nums))
    #print(get_joltage_2("12345", 3))
    #print(get_joltage_2_optimized("12345", 3))
    #print(get_joltage_2_optimized("2222437223345352721242114242243132424423321322342222321424353272152143231321424542434432234244211122", 12))
    #print(get_joltage_2_optimized("818181911112111", 12))

if __name__ == "__main__":
    day_3()

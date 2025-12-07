def day_6_part_2():
    raw = []
    with open("src/day_6/input.txt", "r") as f:
        raw = list(map(lambda x: x.replace('\n',''),f.readlines()))

    operators = raw[len(raw)-1]
    raw = raw[:len(raw)-1]

    nums_formatted = []

    last_seen_op = 0
    for r in raw:
        bucket = []
        for i in range(1,len(operators)):
            if i == len(operators)-1:
                bucket.append(r[last_seen_op:i+1])
                last_seen_op = 0
                continue
            if operators[i] != ' ':
                bucket.append(r[last_seen_op:i-1])
                last_seen_op = i

        nums_formatted.append(bucket)

    clean = [[] for _ in range(len(nums_formatted[0]))]
    for i, row in enumerate(nums_formatted):
        # i is the index of the kth number
        for j, nums in enumerate(row):
            # j is the bucket we're looking at
            for k, num in enumerate(nums):
                # k is the index of the jth bucket
                bucket = clean[j]
                if not bucket or len(bucket) <= k:
                    bucket.append(' '*len(nums_formatted))
                if num == " ":
                    continue
                bucket[k] = bucket[k][:i]+num+bucket[k][i+1:]

    # Go through and convert all values to int
    for i, bucket in enumerate(clean):
        clean[i] = list(map(int, bucket))

    operators = operators.split()
    print(part_1(clean, operators))

def part_1(nums: list[list[int]], operators: list[str]) -> int:
    res = 0

    for i, op in enumerate(operators):
        cur_total = 0 if op == "+" else 1
        for num in nums[i]:
            if op == "+":
                cur_total += num
            else:
                cur_total *= num

        res += cur_total


    return res
def day_6_part_1():
    raw = []
    with open("src/day_6/input.txt", "r") as f:
        raw = list(map(lambda x: x.strip(), f.readlines()))
    operators = raw[len(raw)-1].split()
    nums = [[] for _ in range(len(raw[0].split()))]
    for i in range(len(raw)-1):
        cur = raw[i].split()
        for i in range(len(cur)):
            nums[i].append(int(cur[i]))

    print(part_1(nums, operators))

if __name__ == "__main__":
    #day_6_part_1()
    day_6_part_2()

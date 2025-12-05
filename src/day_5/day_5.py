# In this approach we try and find gaps in the total range, 
# where the total range is the smallest value from all the ranges
# up until the largest value inclusive.
def part_2(ranges: list[list[int]]) -> int:
    min_val = ranges[0][0]
    max_val = ranges[0][1]

    # Get min val and max val for a total range span
    for r in ranges:
        if r[0] < min_val:
            min_val = r[0]

        if r[1] > max_val:
            max_val = r[1]

    ranges.sort()

    # Set current ceiling to largest from first range
    cur_ceil = ranges[0][1]

    bad_ids = 0

    for r in ranges:

        # If the smallest value of the current range is greater than our
        # current ceiling, that MUST indicate a gap. If that gap is greater than
        # 1 it means we've broken up a contiguous block. Add that as a bad ID
        if r[0] > cur_ceil and r[0] - cur_ceil > 1:
            bad_ids += r[0] - cur_ceil - 1

        if r[1] > cur_ceil:
            cur_ceil = r[1]

    # Total range minus bad ids
    return (max_val - min_val + 1) - bad_ids



def is_in_ranges(ranges: list[list[int]], id: int) -> bool:
    for r in ranges:
        # inclusive range
        if id in range(r[0], r[1]+1):
            return True
    return False


def part_1(ranges: list[list[int]], ids: list[int]) -> int:
    res = 0

    for id in ids:
        if is_in_ranges(ranges, id):
            res += 1

    return res
    
def day_5():
    with open("src/day_5/input.txt", "r") as f:
        raw = list(map(lambda x: x.strip(),f.readlines()))

    ranges = []
    ids = []
    ids_start_idx = 0
    for i,r in enumerate(raw):
        if r == "":
            ids_start_idx = i
            break
        r = r.split("-")
        r = [int(r[0]), int(r[1])]
        ranges.append(r)


    ids_start_idx += 1
    while ids_start_idx < len(raw):
        row = raw[ids_start_idx]
        ids.append(int(row))
        ids_start_idx += 1

    print(part_1(ranges,ids))

#    ranges = [
#        [3,5],
#        [10,14],
#        [16,20],
#        [12,18],
#    ]
    print(part_2(ranges))

if __name__ == "__main__":
    day_5()

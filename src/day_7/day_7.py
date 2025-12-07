def part_2(grid: list[list[str]]) -> int:
    cache: dict[tuple[int,int], int] = {}

    grid_len = len(grid)

    def dfs(i: int, level: int) -> int:
        key = (i, level)
        if i < 0 or i >= len(grid[0]):
            return 0

        if level == grid_len - 1:
            cache[key] = 1
            return cache[key]

        if key in cache:
            return cache[key]
        
        if grid[level][i] == "^":
            cache[key] = dfs(i-1, level+1) + dfs(i+1, level+1)
        else:
            cache[key] = dfs(i, level+1)

        return cache[key]

    start_i = 0
    # Find start point
    for i, char in enumerate(grid[0]):
        if char == "S":
            start_i = i

    return dfs(start_i, 1)

def part_1(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    res = 0
    beams = set()

    # Find start point
    for i, char in enumerate(grid[0]):
        if char == "S":
            beams.add(i)

    for row in grid[1:]:
        to_remove = []
        to_add = []
        for beam in beams:
            if row[beam] != "^":
                continue
            else:
                res += 1
                if (beam - 1 >= 0 and 
                    beam - 1 not in beams):
                    to_add.append(beam - 1)
                if (beam + 1 >= 0 and 
                    beam + 1 not in beams):
                    to_add.append(beam + 1)

                to_remove.append(beam)
        for beam in to_add:
            beams.add(beam)
        for beam in to_remove:
            beams.remove(beam)

    return res

def day_7():
    grid = []
    with open("src/day_7/input.txt", "r") as f:
        grid = list(map(lambda x: list(x.strip()), f.readlines()))

    print(part_2(grid))

if __name__ == "__main__":
    day_7()

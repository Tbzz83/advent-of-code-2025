def remove_at(r,c,grid) -> str:
    return grid[r][:c] + "." + grid[r][c+1:] 

def part_2(grid: list[str]) -> int:
    if not grid:
        return 0
    res = [0]
    ROWS, COLS = len(grid), len(grid[0])

    def recurse(r,c):
        # If can be removed, remove it 
        grid[r] = remove_at(r,c,grid)
        res[0] += 1

        backfill = [
            (r-1,c-1),
            (r-1,c+1),
            (r-1,c),
            (r,c-1),
            (r+1,c+1),
            (r+1,c-1),
            (r+1,c),
            (r,c+1)
        ]

        for coord in backfill:
            if is_valid_coord(coord, ROWS, COLS, grid) and is_valid_roll(coord[0], coord[1],ROWS,COLS,grid):
                recurse(coord[0],coord[1])


    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == ".":
                continue

            if is_valid_roll(r,c,ROWS,COLS,grid):
                recurse(r,c)

    for r in grid:
        print(r)
    return res[0]

def is_valid_roll(r, c, ROWS, COLS, grid) -> bool:
    left = (r, c-1)
    right = (r,c+1)
    up = (r-1,c)
    down = (r+1, c)
    d_up_left = (r-1, c-1)
    d_up_right = (r-1, c+1)
    d_down_left = (r+1, c-1)
    d_down_right = (r+1, c+1)
    left = grid[left[0]][left[1]] if is_valid_coord(left, ROWS, COLS, grid) else "."
    right = grid[right[0]][right[1]] if is_valid_coord(right, ROWS, COLS, grid) else "."
    up = grid[up[0]][up[1]] if is_valid_coord(up, ROWS, COLS, grid) else "."
    down = grid[down[0]][down[1]] if is_valid_coord(down, ROWS, COLS, grid) else "."
    d_up_left = grid[d_up_left[0]][d_up_left[1]] if is_valid_coord(d_up_left, ROWS, COLS, grid) else "."
    d_down_left = grid[d_down_left[0]][d_down_left[1]] if is_valid_coord(d_down_left, ROWS, COLS, grid) else "."
    d_down_right = grid[d_down_right[0]][d_down_right[1]] if is_valid_coord(d_down_right, ROWS, COLS, grid) else "."
    d_up_right = grid[d_up_right[0]][d_up_right[1]] if is_valid_coord(d_up_right, ROWS, COLS, grid) else "."
    adj = [left,right,up,down,d_up_left,d_up_right,d_down_left,d_down_right]

    invalids = 0
    for char in adj:
        if char == "@":
            invalids += 1
        if invalids >= 4:
            return False
    return True


def is_valid_coord(coord: tuple[int,int], ROWS: int, COLS: int, grid) -> bool:
    return ((coord[0] < ROWS and coord[0] >= 0) and 
            coord[1] < COLS and coord[1] >= 0 and 
            grid[coord[0]][coord[1]] == "@") 
            

def part_1(grid: list[str]) -> int:
    if not grid:
        return 0

    res: int = 0
    ROWS, COLS = len(grid), len(grid[0])


    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == ".": continue

            if is_valid_roll(r,c, ROWS, COLS,grid):
                res += 1

    return res
    

def day_4():
    with open("src/day_4/input.txt", "r") as f:
        grid = list(map(lambda x: x.strip(), f.readlines()))
#    grid = [
#        "..@@.@@@@.",
#        "@@@.@.@.@@",
#        "@@@@@.@.@@",
#        "@.@@@@..@.",
#        "@@.@@@@.@@",
#        ".@@@@@@@.@",
#        ".@.@.@.@@@",
#        "@.@@@.@@@@",
#        ".@@@@@@@@.",
#        "@.@.@@@.@.",
#    ]
    #print(part_1(grid))
    print(part_2(grid))

if __name__ == "__main__":
    day_4()

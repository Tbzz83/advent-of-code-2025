from collections import defaultdict
from collections import deque

# PART 2 TODO INVESTIGATE POINT IN POLYGON
# https://en.wikipedia.org/wiki/Point_in_polygon

def get_legal_coords(coords: list[list[int]]) -> tuple[set[tuple[int,int]], int, int]:
    legal: set[tuple[int,int]] = set()
    x_max, y_max = 0,0

    i = 0
    for i, cur_coord in enumerate(coords): 
        prev_coord = coords[i-1] if i-1 >= 0 else coords[len(coords)-1]
        next_coord = coords[i+1] if i+1 < len(coords) else coords[0]

        x1, y1 = cur_coord

        if x1 > x_max: 
            x_max = x1
        if y1 > y_max: 
            y_max = y1

        x0, y0 = prev_coord
        x2, y2 = next_coord

        # Get valid coords b/w cur and prev
        if x1 == x0:
            start, stop = y0, y1
            if y1 < y0:
                start, stop  = y1, y0
            for i in range(start+1, stop):
                legal.add((x1, i))
        elif y1 == y0:
            start, stop = x0, x1
            if x1 < x0:
                start, stop  = x1, x0
            for i in range(start+1, stop):
                legal.add((i, y1))
        else:
            # Shouldn't ever happend
            raise Exception(f"Straight line can't be found between {cur_coord} and {prev_coord}")

        # Get valid coords b/w cur and next
        if x1 == x2:
            start, stop = y2, y1
            if y1 < y2:
                start, stop  = y1, y2
            for i in range(start+1, stop):
                legal.add((x1, i))
        elif y1 == y2:
            start, stop = x2, x1
            if x1 < x2:
                start, stop  = x1, x2
            for i in range(start+1, stop):
                legal.add((i, y1))
        else:
            # Shouldn't ever happend
            raise Exception(f"Straight line can't be found between {cur_coord} and {prev_coord}")


        legal.add((x1,y1))

    return legal, x_max, y_max

def build_area_adj_list_1(coords: list[list[int]]) -> tuple[dict[int, list[tuple[int,int]]], int]:
    adj_list: dict[int, list[tuple[int,int]]] = defaultdict(list)

    seen_pairs: set[tuple[int,int]] = set()
    largest = 0

    for i, coord_i in enumerate(coords):
        x1, y1 = coord_i

        for j, coord_j in enumerate(coords):
            if (i,j) in seen_pairs or (j, i) in seen_pairs or i == j:
                continue
            x2, y2 = coord_j

            if x1 != x2 and y1 != y2:
                area: int = ((abs(x2-x1) + 1) * (abs(y2-y1) + 1))
            elif x1 == x2:
                area: int = abs(y2-y1) + 1
            else:
                area: int = abs(x2-x1) + 1

            if area > largest:
                largest = area

            adj_list[i].append((j,area))
            adj_list[j].append((i,area))

            seen_pairs.add((i,j))

    return adj_list, largest

    
def get_illegal_coords(legal_coords: set[tuple[int,int]], x_max: int, y_max: int) -> set[tuple[int,int]]:
    illegal: set[tuple[int,int]] = set()
    q = deque()
    q.append((0,0))

    def add_to_q(x,y):
        if x in range(x_max+1) and y in range(y_max+1) and (x,y) not in legal_coords and (x,y) not in illegal:
            q.append((x,y))

    while q:
        x,y = q.popleft()

        illegal.add((x,y))

        dirs = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
        for dir in dirs:
            add_to_q(dir[0],dir[1])

    return illegal

def get_max_area(coords: list[list[int]], illegal: set[tuple[int,int]]) -> int:
    seen_pairs: set[tuple[int,int]] = set()
    largest = 0

    for i, coord_i in enumerate(coords):
        x1, y1 = coord_i

        for j, coord_j in enumerate(coords):
            if (i,j) in seen_pairs or (j, i) in seen_pairs or i == j:
                continue
            x2, y2 = coord_j

            x3, y3 = x1,y2
            x4, y4 = x2,y1

            # Only consider legal squares
            if (
                (x3,y3) in illegal or
                (x4,y4) in illegal):
                continue

            if x1 != x2 and y1 != y2:
                area: int = ((abs(x2-x1) + 1) * (abs(y2-y1) + 1))
            elif x1 == x2:
                area: int = abs(y2-y1) + 1
            else:
                area: int = abs(x2-x1) + 1

            if area > largest:
                largest = area

            seen_pairs.add((i,j))

    return largest


def part_2(coords: list[list[int]]) -> int:

    legal, x_max, y_max = get_legal_coords(coords)
    print(len(legal))

    #illegal = get_illegal_coords(legal, x_max, y_max)

    #return get_max_area(coords, illegal)
    return 0

def part_1(coords: list[list[int]]) -> int:
    _, largest = build_area_adj_list_1(coords)

    return largest

def day_9():
    coords = []
    with open("src/day_9/test.txt", "r") as f:
        coords = list(map(lambda x: [ int(y) for y in x.strip().split(",")],f.readlines()))

    #print(part_1(coords))
    print(part_2(coords))
    

if __name__ == "__main__":
    day_9()

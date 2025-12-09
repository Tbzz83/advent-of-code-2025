from collections import defaultdict
def build_area_adj_list(coords: list[list[int]]) -> tuple[dict[int, list[tuple[int,int]]], int]:
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

    

def part_1(coords: list[list[int]]) -> int:
    _, largest = build_area_adj_list(coords)

    return largest

def day_9():
    coords = []
    with open("src/day_9/test.txt", "r") as f:
        coords = list(map(lambda x: [ int(y) for y in x.strip().split(",")],f.readlines()))

    print(part_1(coords))
    

if __name__ == "__main__":
    day_9()

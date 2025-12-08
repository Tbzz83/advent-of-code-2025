import math
import heapq
from collections import defaultdict
from collections import defaultdict

def part_2(coords: list[list[int]]) -> int:
    res = 0

    adj_map = build_adj_map(coords)

    distances_t: list[list[int]] = []

    for i, distances in adj_map.items():
        for j, distance in distances:
            if i == j:
                continue
            distances_t.append([distance,i, j])

    distances_t.sort()

    circuits = {}
    for k in range(len(distances_t)):
        i, j = distances_t[k][1], distances_t[k][2]

        if i not in circuits and j not in circuits:
            new_circuit = Circuit()
            new_circuit.append(i)
            new_circuit.append(j)
            circuits[i] = new_circuit
            circuits[j] = new_circuit

        elif i not in circuits:
            circuit = circuits[j]
            circuit.append(i)
            circuits[i] = circuit
        elif i not in circuits:
            circuit = circuits[i]
            circuit.append(j)
            circuits[j] = circuit
        elif i in circuits and j in circuits:
            circ_i, circ_j = circuits[i], circuits[j]
            if circ_i.id != circ_j.id:
                # COALESCE EVENT
                merge = Circuit()
                merge.extend(circ_i + circ_j)
                for l in merge:
                    circuits[l] = merge

        if len(circuits[i]) == len(coords):
            print("CASE")
            return coords[i][0] * coords[j][0]

    return res

def build_adj_map(coords: list[list[int]]):
    adj_map: dict[int, list[tuple[int,int]]] = {}

    # i is cur
    for i in range(len(coords)):
        # j is all others
        for j in range(len(coords)):
            if i == j:
                continue
            if i not in adj_map:
                adj_map[i] = []
            if j not in adj_map:
                adj_map[j] = []

            dx = coords[i][0] - coords[j][0]
            dy = coords[i][1] - coords[j][1]
            dz = coords[i][2] - coords[j][2]

            dist = int(math.sqrt(dx*dx + dy*dy + dz*dz))

            adj_map[i].append((j, dist))

    return adj_map

class Circuit(list):
    id_counter = 0

    def __init__(self, *args) -> None:
        super().__init__(args)
        self.id = Circuit.id_counter
        Circuit.id_counter += 1

def part_1(coords: list[list[int]], n=1000) -> int:
    res = 1
    adj_map = build_adj_map(coords)

    distances_t: list[list[int]] = []
    min_map: dict[int, set[int]] = defaultdict(set)

    for i, distances in adj_map.items():
        for j, distance in distances:
            if i == j:
                continue
            distances_t.append([distance,i, j])

    distances_t.sort()
    circuits = {}

    for i in range(2*n):
        if i >= len(distances_t):
            break
        obj = distances_t[i]
        i,j = obj[1], obj[2]
#
#        if i not in circuits and j not in circuits:
#            new_circuit = Circuit()
#            new_circuit.append(i)
#            new_circuit.append(j)
#            circuits[i] = new_circuit
#            circuits[j] = new_circuit
#        elif i not in circuits:
#            circuit = circuits[j]
#            circuit.append(i)
#            circuits[i] = circuit
#        elif j not in circuits:
#            circuit = circuits[i]
#            circuit.append(j)
#            circuits[j] = circuit
#        # MERGE CIRCUITS
#        elif circuits[i].id != circuits[j].id:
#            print("CASE", circuits[i], circuits[j], i, j)
#            i_circuit, j_circuit = circuits[i], circuits[j]
#            merged = Circuit()
#            merged.extend(i_circuit + j_circuit)
#            for i in merged:
#                circuits[i] = merged
#        else:
#            continue

        min_map[i].add(j)
        min_map[j].add(i)

    seen: set = set()

    def dfs(i, cycle: set = set(), parent: int = -1) -> int:
        if i in seen:
            return 0

        nodes = 1
        seen.add(i)
        cycle.add(i)

        for child in min_map[i]:
            if child == parent:
                continue
            nodes += dfs(child, cycle, i)

        #cycle.remove(i)
        return nodes

    lengths = []

    for i in range(len(coords)):
        if i not in seen:
            heapq.heappush(lengths, -dfs(i))

    print(lengths)

    for _ in range(3):
        popped = -heapq.heappop(lengths)
        res *= popped

    return res

#    for i, distances in adj_map.items():
#        min_j, min_distance = distances[0]
#        for j, distance in distances:
#            if distance < min_distance:
#                min_distance = distance
#                min_j = j
#
#        if i not in circuits and min_j not in circuits:
#            new_circuit = Circuit()
#            new_circuit.append(i)
#            new_circuit.append(min_j)
#            circuits[i] = new_circuit
#            circuits[min_j] = new_circuit
#        elif i not in circuits:
#            circuit = circuits[min_j]
#            circuit.append(i)
#            circuits[i] = circuit
#        elif min_j not in circuits:
#            circuit = circuits[i]
#            circuit.append(min_j)
#            circuits[min_j] = circuit
#        # MERGE CIRCUITS
#        elif circuits[i].id != circuits[min_j].id:
#            print("CASE", circuits[i], circuits[min_j], i, min_j)
#            i_circuit, j_circuit = circuits[i], circuits[min_j]
#            merged = Circuit()
#            merged.extend(i_circuit + j_circuit)
#            for i in merged:
#                circuits[i] = merged
#
#    print("___")
#    print(circuits[7])
#    print("___")
#    seen_ids = set()
#    largest = []
#    for circuit in circuits.values():
#        if circuit.id in seen_ids:
#            continue
#        heapq.heappush(largest, -len(circuit))
#        seen_ids.add(circuit.id)
#
#    for _ in range(3):
#        popped = -heapq.heappop(largest)
#        print(popped)
#        res *= popped
#
#    return res

def day_8():
    coords = []

    with open("src/day_8/input.txt", "r") as f:
        coords = list(map(lambda x: [int(y) for y in x.strip().split(",")], f.readlines()))

    #print(part_1(coords))
    print(part_2(coords))

if __name__ == "__main__":
    day_8()

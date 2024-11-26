
def sovle_puzzle(start_r, start_c, end_r, end_c, puzzle: list[list[int]]):
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    visited = set()
    deq = []
    visited.add((start_r, start_c))
    deq.append((start_r, start_c))

    while len(deq)!=0:
        node_r, node_c = deq.pop(0)
        for dr, dc in moves:
            new_r = node_r + dr
            new_c = node_c + dc
            if not (0<=new_r<len(puzzle) and 0<=new_c<len(puzzle[0])):
                continue
            if puzzle[new_r][new_c] == 1:
                continue
            if (new_r, new_c) in visited:
                continue
            if new_r==end_r and new_c==end_c:
                return True
            visited.add((new_r, new_c))
            deq.append((new_r, new_c))
    return False

def main():
    matrix = [[1, 0, 0, 0, 1],
              [1, 1, 0, 1, 1],
              [1, 1, 0, 1, 1],
              [1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0]]
    print(sovle_puzzle(4, 1, 3, 4, matrix))

if __name__=='__main__':
    main()

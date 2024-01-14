from collections import deque

def is_valid_move(row, col, maze, visited):
    rows, cols = len(maze), len(maze[0])
    return 0 <= row < rows and 0 <= col < cols and maze[row][col] != 1 and not visited[row][col]

def get_neighbors(row, col, maze, visited):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid_move(new_row, new_col, maze, visited):
            neighbors.append((new_row, new_col))

    return neighbors

def shortest_path_length(maze, start, target):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]

    queue = deque([(start[0], start[1], 0, 0)])  # (row, col, distance, num_twos)
    visited[start[0]][start[1]] = True

    while queue:
        row, col, distance, num_twos = queue.popleft()

        if (row, col) == (target[0], target[1]):
            return distance

        neighbors = get_neighbors(row, col, maze, visited)

        for neighbor_row, neighbor_col in neighbors:
            new_distance = distance + 2
            new_num_twos = num_twos + (maze[neighbor_row][neighbor_col] == 2)

            if new_num_twos <= 2:  # Constraint: at most 2 blocks with value 2
                queue.append((neighbor_row, neighbor_col, new_distance, new_num_twos))
                visited[neighbor_row][neighbor_col] = True

    return "STUCK"

# Input
rows, cols = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(rows)]
start = tuple(map(int, input().split()))
target = tuple(map(int, input().split()))

# Output
result = shortest_path_length(maze, start, target)
print(result)
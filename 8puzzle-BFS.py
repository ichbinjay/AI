from shutil import move


def calculate_fn(state):
    fn = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[0][i][j]:
                fn += 1
    return fn


import copy

def move(state):
    results = []
    row = ind = None
    s_state = state[0].copy()
    for i in s_state:
        if 0 in i:
            row = s_state.index(i)
            ind = i.index(0)
            break

    # Move Up
    if ind != 0:
        s_state[row][ind], s_state[row][ind - 1] = s_state[row][ind - 1], s_state[row][ind]
        fn = calculate_fn(s_state)
        results.append((copy.deepcopy(s_state), fn))
        s_state[row][ind], s_state[row][ind - 1] = s_state[row][ind - 1], s_state[row][ind]

    # Move Down
    if ind != 2:
        s_state[row][ind], s_state[row][ind + 1] = s_state[row][ind + 1], s_state[row][ind]
        fn = calculate_fn(s_state)
        results.append((copy.deepcopy(s_state), fn))
        s_state[row][ind], s_state[row][ind + 1] = s_state[row][ind + 1], s_state[row][ind]

    # Move Left
    if row != 0:
        s_state[row][ind], s_state[row - 1][ind] = s_state[row - 1][ind], s_state[row][ind]
        fn = calculate_fn(s_state)
        results.append((copy.deepcopy(s_state), fn))
        s_state[row][ind], s_state[row - 1][ind] = s_state[row - 1][ind], s_state[row][ind]

    # Move Right
    if row != 2:
        s_state[row][ind], s_state[row + 1][ind] = s_state[row + 1][ind], s_state[row][ind]
        fn = calculate_fn(s_state)
        results.append((copy.deepcopy(s_state), fn))
        s_state[row][ind], s_state[row + 1][ind] = s_state[row + 1][ind], s_state[row][ind]

    return results


def solve():
    # Create a queue for BFS
    queue = []
    # Mark the source node as visited and enqueue it
    visited = set()
    queue.append(start)
    visited.add(tuple(map(tuple, start[0])))
    while queue:
        # Dequeue a vertex from queue
        s = queue.pop(0)
        print(s)
        # If this adjacent node is the goal node, then return true
        if s[0] == goal[0]:
            print("Goal Found")
            return
        # Else, continue to do BFS
        for i, j in move(s):
            if tuple(map(tuple, i)) not in visited:
                queue.append([i, j])
                visited.add(tuple(map(tuple, i)))
        queue.sort(key=lambda x: x[1])
    print("No Solution")
    return


goal = [[[1, 2, 3], [4, 5, 6], [7, 8, 0]], 0]
start = [[[1, 2, 3], [4, 5, 6], [7, 0, 8]], 0]
solve()

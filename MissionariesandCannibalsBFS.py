from collections import deque

def isPossible(current, cannibals, missionaries):
    if cannibals + missionaries > 2 or cannibals + missionaries == 0:
        return False

    if current[-1] == 1:
        if current[0] - cannibals < 0 or current[1] - missionaries < 0:
            return False
        else:
            return True
    else:
        if current[2] - cannibals < 0 or current[3] - missionaries < 0:
            return False
        else:
            return True


def successors(current):
    result = []
    for cannibals in range(3):
        for missionaries in range(3):
            if isPossible(current, cannibals, missionaries):
                new = current[:]
                if new[-1] == 1:
                    new[0] -= cannibals
                    new[1] -= missionaries
                    new[2] += cannibals
                    new[3] += missionaries
                    new[4] = 0
                else:
                    new[0] += cannibals
                    new[1] += missionaries
                    new[2] -= cannibals
                    new[3] -= missionaries
                    new[4] = 1
                result.append(new)
    return result


def isValid(current):
    if current[0] > current[1] and current[1] != 0:
        return False
    elif current[2] > current[3] and current[3] != 0:
        return False
    return True


def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]
        visited.add(tuple(state))
        for succ in successors(state):
            if tuple(succ) not in visited and isValid(succ):
                queue.append((succ, path + [state]))
    return None


if __name__ == "__main__":
    start = [3, 3, 0, 0, 1]
    goal = [0, 0, 3, 3, 0]
    path = bfs(start, goal)
    if path is not None:
        print("Success!")
        for i, state in enumerate(path):
            print("Step {}: Left Bank: {}C, {}M, Right Bank: {}C, {}M".format(i+1, state[0], state[1], state[2], state[3]))
    else:
        print("Failed!")

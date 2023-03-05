def move(current):
    # water jug problem
    if current[0] == 0:
        current[0] = 4
    elif current[1] < 3:
        if current[0] >= 3 - current[1]:
            current[0] -= 3 - current[1]
            current[1] = 3
        else:
            current[1] += current[0]
            current[0] = 0
    elif current[1] == 3:
        current[1] = 0
    return current

if __name__ == "__main__":
    start = [0, 0]
    goal = [[2, 0],[2,1],[2,2]]
    current = start
    step_count = 0
    # water jug problem
    while current not in goal:
        current = move(current)
        print("Step {}: {}".format(step_count+1, current))
        step_count += 1

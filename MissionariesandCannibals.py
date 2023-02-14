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


def successor(current):
    if current[-1] == 1:
        print("Boat is on the left side")
    else:
        print("Boat is on the right side")
    cannibals = int(input("Enter number of cannibals: "))
    missionaries = int(input("Enter number of missionaries: "))
    if isPossible(current, cannibals, missionaries):
        if current[-1] == 1:
            current[0] -= cannibals
            current[1] -= missionaries
            current[2] += cannibals
            current[3] += missionaries
            current[4] = 0
        else:
            current[0] += cannibals
            current[1] += missionaries
            current[2] -= cannibals
            current[3] -= missionaries
            current[4] = 1
        print("Current state: Left Bank: {}C, {}M, Right Bank: {}C, {}M".format(current[0], current[1], current[2], current[3]))
        return current
    else:
        print("Invalid move!")
        return current


def isValid(current):
    if current[0] > current[1] and current[1] != 0:
        return False
    elif current[2] > current[3] and current[3] != 0:
        return False
    return True


if __name__ == "__main__":
    current = [3, 3, 0, 0, 1]
    goal = [0, 0,3, 3, 0]
    flag = True
    # left = 1, right = 0
    print("Current state: Left Bank: {}C, {}M, Right Bank: {}C, {}M".format(current[0], current[1], current[2], current[3]))
    print("Goal state: Left Bank: {}C, {}M, Right Bank: {}C, {}M\n".format(goal[0], goal[1], goal[2], goal[3]))
    while current != goal:
        new = successor(current)
        if isValid(new):
            current = new
        else:
            print("Failed!")
            flag = False
            break
    if flag:
        print("Success!")

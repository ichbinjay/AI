from queue import PriorityQueue

def calculateH(current, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            if current[i][j] != goal[i][j]:
                h += 1
    return h

def generate_next_moves(current):
    res = []
    for i in range(3):
        for j in range(3):
            if current[i][j] == 0:
                if i > 0:
                    temp = current.copy()
                    temp[i][j] = temp[i-1][j]
                    temp[i-1][j] = 0
                    res.append(temp)
                if i < 2:
                    temp = current.copy()
                    temp[i][j] = temp[i+1][j]
                    temp[i+1][j] = 0
                    res.append(temp)
                if j > 0:
                    temp = current.copy()
                    temp[i][j] = temp[i][j-1]
                    temp[i][j-1] = 0
                    res.append(temp)
                if j < 2:
                    temp = current.copy()
                    temp[i][j] = temp[i][j+1]
                    temp[i][j+1] = 0
                    res.append(temp)
    return res

def solve(start, goal, moves):
    q = PriorityQueue()
    q.put((calculateH(start, goal), start))

    visited = set()

    while not q.empty():
        current = q.get()
        if current[1] == goal:
            print("Solved in " + str(moves[0]) + " moves!")
            return
        else:
            visited.add(tuple(map(tuple, current[1])))
            moves[0] += 1
            if moves[0] > 1000:
                print("Could not solve in 1000 moves.")
                return
            print("Move: " + str(moves[0]))
            print(current[1])
            print()
            next_moves = generate_next_moves(current[1])
            for move in next_moves:
                if tuple(map(tuple, move)) not in visited:
                    q.put((calculateH(move, goal), move))

def main():
    start = [[1,2,3],[4,6,8],[7,5,0]]
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    moves = [0]
    solve(start, goal, moves)

main()

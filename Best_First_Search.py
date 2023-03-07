def bfs():
    # IPS: start, goal, h, matrix
    # OPS: path, cost
    # BEST FIRST SEARCH
    open, closed = [], []
    open.append(ord(start) - 65)
    while open:
        open.sort(key=lambda x: h[chr(x + 65)])
        current = open.pop(0)
        closed.append(current)
        if chr(current + 65) == goal:
            break
        else:
            for i in range(len(matrix[current])):
                if matrix[current][i] == 1 and i not in closed:
                    open.append(i)

            # Remove failed nodes from open list
            open = [node for node in open if h[chr(node + 65)] < h[chr(current + 65)]]

    path = [chr(i + 65) for i in closed]
    cost = sum([h[x] for x in path])
    return path, cost


'''matrix = [[0,1,1,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]
start = 'A'
goal = 'H'
h = {"A":13,"B":12,"C":4, "D":7,"E":3,"F":8,"H":0,"I":4,"J":9,"G":2}
print(bfs())'''
'''
matrix = [[0,1,1,0,0],
          [0,0,0,1,1],
          [0,0,0,1,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]
start = 'A'
goal = 'D'
h = {"A":3, "B": 2, "C": 1, "D": 0, "E": 0}
print(bfs())'''

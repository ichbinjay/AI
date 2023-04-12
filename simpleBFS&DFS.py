def bfs_traversal():
    visited = [False] * len(matrix)
    queue = []
    queue.append(0)
    visited[0] = True
    while queue:
        node = queue.pop(0)
        # print corresponding alphabet for current node
        print(chr(node + ord('A')), end=" ")
        for i in range(len(matrix)):
            if matrix[node][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True

def dfs_traversal():
    visited = [False] * len(matrix)
    stack = []
    stack.append(0)
    visited[0] = True
    while stack:
        node = stack.pop(-1)
        # print corresponding alphabet for current node
        print(chr(node + ord('A')), end=" ")
        for i in range(len(matrix)):
            if matrix[node][i] == 1 and visited[i] == False:
                stack.append(i)
                visited[i] = True

matrix = [[0,1,1,0,0],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
'''
        A
      /   \
    B      C
   / \     
  D   E
'''
print(bfs_traversal())
print(dfs_traversal())

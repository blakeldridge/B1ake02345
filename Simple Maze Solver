maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

start = 1,1
end = 8,7

matrix = []
for i in range(len(maze)):
    matrix.append([])
    for j in range(len(maze[i])):
        matrix[-1].append(0)

i,j = start
matrix[i][j] = 1


def make_step(k):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == k:
                if i>0 and matrix[i-1][j] == 0 and maze[i-1][j] == 0:
                    matrix[i-1][j] = k + 1
                if i<len(matrix)-1 and matrix[i+1][j] == 0 and maze[i+1][j] == 0:
                    matrix[i+1][j] = k + 1
                if j<len(matrix[i])-1 and matrix[i][j+1] == 0 and maze[i][j+1] == 0:
                    matrix[i][j+1] = k + 1
                if j>0 and matrix[i][j-1] == 0 and maze[i][j-1] == 0:
                    matrix[i][j-1] = k + 1


k = 0
while matrix[end[0]][end[1]] == 0:
    k += 1
    make_step(k)
    
i,j = end
k = matrix[i][j]
the_path = [(i,j)]
while k > 1:
    if i > 0 and matrix[i-1][j] == k-1:
        i,j = i-1,j
        the_path.append((i,j))
        k -= 1
    if i<len(matrix) - 1 and matrix[i+1][j] == k-1:
        i,j = i+1,j
        the_path.append((i,j))
        k -= 1
    if j>0 and matrix[i][j-1] == k-1:
        i,j = i,j-1
        the_path.append((i,j))
        k -= 1
    if j<len(matrix[i])-1 and matrix[i][j+1] == k-1:
        i,j = i,j+1
        the_path.append((i,j))
        k -= 1

completedMaze = []
for i in range(len(maze)):
    completedMaze.append([])
    for j in range(len(maze[i])):
        completedMaze[-1].append(0)

for coords in the_path:
    completedMaze[coords[0]][coords[1]] = 1
print('original maze: ')
print(maze)
print('solved maze: ')
print (completedMaze)

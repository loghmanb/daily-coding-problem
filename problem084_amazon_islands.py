'''
This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. 
A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1

'''

def addIsland(pos, visited, mat):
    i, j = pos
    if i<0 or j<0 or i>=len(mat) or j>=len(mat[i]) \
            or not mat[pos[0]][pos[1]] \
            or pos in visited:
        return
    visited.add(pos)
    addIsland((i, j-1), visited, mat)
    addIsland((i, j+1), visited, mat)
    addIsland((i-1, j), visited, mat)
    addIsland((i+1, j), visited, mat)


def noOfIslands(mat):
    islasnds = {}
    visited = set()

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] and (i, j) not in visited:
                islasnds[(i, j)] = True
                visited.add((i, j))
                addIsland((i, j+1), visited, mat)
                addIsland((i+1, j), visited, mat)
    return len(islasnds.keys())


if __name__ == "__main__":
    data = [
            [
                [
                    [1, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 1, 0, 0, 1],
                    [1, 1, 0, 0, 1],
                ],
                4
            ]
    ]
    for d in data:
        print('input', d[0], 'output', noOfIslands(d[0]))
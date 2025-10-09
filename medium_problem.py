#  Given an n x m grid of 'W' (Water) and 'L' (Land), the task is to count the number of islands.
# An island is a group of adjacent 'L' cells connected horizontally, vertically, or diagonally, 
# and it is surrounded by water or the grid boundary.
# The goal is to determine how many distinct islands exist in the grid.


# this function takes the current position adn saves it into stack array.
# then pops the element saved into new x,y vars (stack is now null)
# then checks each direction considering the conditions, not out of bounds, its an 'L', and not visited
# then when found 'L' it continues the search using by appending the new 'L' position into stack
# repeats the process until no connected 'L' is found
def checkSurrounding(grid, x, y, visited):
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0,1),
                  (1,-1),  (1,0),  (1,1)]
    
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))


def countIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    # this creates a boolean grid to mark visited lands
    visited = [[False]*cols for _ in range(rows)]
    numIsland = 0

    # increase number of islands after finding new islands not connected to previous islands
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'L' and not visited[i][j]:
                checkSurrounding(grid, i, j, visited)
                numIsland += 1

    return numIsland


grid = [
    ['L','L','W','W','W'],
    ['W','L','W','W','L'],
    ['L','W','W','L','L'],
    ['W','W','W','W','W'],
    ['L','W','L','L','W']
]

print("Number of islands:", countIslands(grid))

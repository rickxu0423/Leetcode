def orangesRotting(grid):
    visitedRot = set()
    round = 0
    def rot(i, j):
        if (i, j) in visitedRot: return False
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if grid[i][j] == 1: 
            grid[i][j] = 2
            return True
    while True:
        rotten = []
        hasFresh = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2 and (i, j) not in visitedRot:
                    rotten.append((i, j))
                    visitedRot.add((i,j))
                if grid[i][j] == 1: hasFresh = True
        if not rotten:
            if hasFresh: return -1
            else: return max(0, round - 1)
        for i,j in rotten:
            rot(i-1, j)
            rot(i, j-1)
            rot(i+1, j)
            rot(i, j+1)       
            
        round += 1

grid = [[2,1,1],[1,1,0],[0,1,1]]

print(orangesRotting(grid)) #4
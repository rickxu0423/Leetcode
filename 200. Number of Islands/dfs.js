var numIslands = function(grid) {
    if (grid == null || grid.length == 0) {
        return 0;
    };
    const amax = grid.length;
    const bmax = grid[0].length;
    function dfs(grid, i ,j) {
        if (i < 0 || j < 0 || i >= amax || j >= bmax || grid[i][j] == 0) {
            return;
        }
        grid[i][j] = 0;
        dfs(grid, i+1, j);
        dfs(grid, i-1, j);
        dfs(grid, i, j+1);
        dfs(grid, i, j-1);
        
    };
    var counter = 0;
    for (var a = 0; a < amax; a++) {
        for (var b = 0; b < bmax; b++) {
            if (grid[a][b] == 1) {
                counter += 1;
                dfs(grid, a, b);
            };
        };
    };
    return counter
};

var grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
console.log(numIslands(grid))
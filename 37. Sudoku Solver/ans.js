var solveSudoku = function(board) {
    
    function could_place(d, row, col) {
        return !( rows[row][d] || columns[col][d] || boxes[box_index(row, col)][d] );
    }
    
    function place_number(d, row, col) {
        rows[row][d] = 1;
        columns[col][d] = 1;
        boxes[box_index(row, col)][d] = 1;
        board[row][col] = d.toString();
    }
    
    function remove_number(d, row, col) {
        delete rows[row][d];
        delete columns[col][d];
        delete boxes[box_index(row, col)][d];
        board[row][col] = ".";
    }
    
    function place_next_numbers(row, col) {
        if (col == 8 && row == 8) {
            sudoku_solved = true;
        } else {
            if (col == 8) backtrack(row + 1, 0);
            else backtrack(row, col + 1);
        }
    }
    
    function backtrack(row=0, col=0) {
        if (board[row][col] == ".") {
            for (var d = 1; d < 10; d++) {
                if (could_place(d, row, col)) {
                    place_number(d, row, col);
                    place_next_numbers(row, col);
                    if (!sudoku_solved) {
                        remove_number(d, row, col);
                    }
                }
            }
        } else place_next_numbers(row, col);
    }
    
    var box_index = (row, col) => Math.floor(row / 3) * 3 + Math.floor(col / 3);
    
    var [rows, columns, boxes] = [{}, {}, {}];
    
    for (var r = 0; r < 9; r++) {
        [rows[r], columns[r], boxes[r]] = [{}, {}, {}];
    }
    
    for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {
            if (board[i][j] != ".") {
                let d = board[i][j];
                place_number(d, i, j);
            }
        }
    }
    
    sudoku_solved = false;
    
    backtrack();
    
    return board;
    
};

const board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]];

console.log(solveSudoku(board)); //[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
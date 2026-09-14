function dfsNQueens(n){
    if(n<1){
        return[];
    }
    const result = [];
    function isValid(board,row,col){
        for (let prevRow=0;prevRow<row;prevRow++){
            const prevCol=board[prevRow];
            if(prevCol===col || Math.abs(prevCol-col)=== row - prevRow){
                return false;
            }
        }
        return true;
    }
    function backtrack(board,row){
        if(row===n){
            result.push([...board]);
            return;
        }
        for(let col=0;col<n;col++){
            if(isValid(board,row,col)){
                board.push(col);
                backtrack(board,row+1);
                board.pop();
            }
        }
    }
    backtrack([],0);
    return result;
}
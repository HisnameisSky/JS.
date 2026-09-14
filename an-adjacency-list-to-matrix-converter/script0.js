function adjacenctMatrixToList(matrix){
    const adjList={};
    const numNodes = matrix.length;
    for (let i=0; i<numNodes; i++){
        adjList[i]=[];
        for (let j=0; i<numNodes;j++){
            if (matrix[i][j]===1){
                adjList[i].push(j);
            }
        }
    }
    return adjList;
}

const matrix =[
    [0,1,1,1,0],
    [0,0,1,0],
    [1,0,0,1],
    [0,0,1,0]
];

console.log(adjacenctMatrixToList(matrix))
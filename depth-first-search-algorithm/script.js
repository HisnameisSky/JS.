function dfs(graph,root){
    const stack = [root];
    const visited = new Set();
    const result = [];
    while (stack.length>0){
        const current = stack.pop();
        if(!visited.has(current)){
            visited.add(current);
            result.push(current);

            for(let neighbor=0; neighbor<graph[current].length; neighbor++){
                if(graph[current][neighbor]===1 && !visited.has(neighbor)){
                    stack.push(neighbor)
                }
            }
        }
    }
    return result;
}
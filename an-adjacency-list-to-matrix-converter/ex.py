from typing import List, Dict
def matrix_to_adjacency_list(matrix: List[List[int]])->Dict[int,List[int]]:
    adj_list={}
    for i, row in enumerate(matrix):
        adj_list[i]=[j for j , val in enumerate(row)if val == 1]
    return adj_list

if __name__ == "__main__":
    matrix = [
        [0,1,1,0],
        [1,0,0,1],[1,0,0,1],[0,1,1,0]
    ]
    adj_list = matrix_to_adjacency_list(matrix)
    print(adj_list)
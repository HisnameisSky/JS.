def adjacenct_matrix_to_list(matrix:list)->dict:
    adj_list=[]
    num_nodes = len(matrix)
    for i in range(num_nodes):
        adj_list[i] = [j for j, val in enumerate(matrix[i]) if val == 1]    
    return adj_list

if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 0]
    ]
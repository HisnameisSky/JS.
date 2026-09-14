def adjacency_list_to_matrix(adj_list: dict) -> list:
    # ノード数（辞書のキーの数）を取得
    num_nodes = len(adj_list)

    # num_nodes x num_nodes の 2次元リスト（0初期化）を生成
    matrix = [[0] * num_nodes for _ in range(num_nodes)]

    # 隣接リストをループ処理して行列に 1 を設定
    for node, neighbors in adj_list.items():
        row = int(node)
        for neighbor in neighbors:
            matrix[row][neighbor] = 1

    # 行列の各行を出力
    for row in matrix:
        print(row)

    return matrix


# === 動作確認 ===
if __name__ == "__main__":
    # 例1: 有向グラフ
    sample_list_1 = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [2]
    }
    print("--- 例1 ---")
    res1 = adjacency_list_to_matrix(sample_list_1)
    
    # 例2: 孤立ノードを含むグラフ
    sample_list_2 = {
        0: [],
        1: [],
        2: []
    }
    print("\n--- 例2 ---")
    res2 = adjacency_list_to_matrix(sample_list_2)
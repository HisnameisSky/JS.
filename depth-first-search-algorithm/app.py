def dfs(graph: list, root: int) -> list:
    # Pythonのリストをスタックとして利用 (LIFO: 後入れ先出し)
    stack = [root]
    
    # 訪問済みのノードを記録するSet (O(1)で検索可能)
    visited = set()
    
    # 最終的な訪問順序を格納するリスト
    result = []

    while stack:
        # スタックの最後尾から要素を取り出す
        current = stack.pop()

        if current not in visited:
            # 未訪問なら訪問済みにマークし、結果リストに追加
            visited.add(current)
            result.append(current)

            # 隣接行列をチェックし、つながっている未訪問ノードをスタックに積む
            # enumerateを使うとインデックス(neighbor)と値(is_connected)を同時に取得可能
            for neighbor, is_connected in enumerate(graph[current]):
                if is_connected == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return result


# === 動作確認 ===
if __name__ == "__main__":
    matrix1 = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    
    print(dfs(matrix1, 1))
    # 出力: [1, 2, 3, 0]

    matrix2 = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ]
    print(dfs(matrix2, 3))
    # 出力: [3, 2] (0と1には繋がっていないため探索されない)
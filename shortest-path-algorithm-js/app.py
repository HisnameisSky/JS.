import math

# 無限大（INF）の定義
INF = math.inf

# 隣接行列（Adjacency Matrix）
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]


def shortest_path(matrix, start_node, target_node=None):
    n = len(matrix)

    # 各ノードへの最短距離（初期値はすべて INF、開始ノードのみ 0）
    distances = [INF] * n
    distances[start_node] = 0

    # 最短経路の履歴リスト（初期値は各ノード自身のみ）
    paths = [[i] for i in range(n)]

    # 訪問済みフラグのリスト
    visited = [False] * n

    for _ in range(n):
        min_distance = INF
        current = -1

        # 未訪問ノードの中から最も距離が短いノードを選択
        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        # 訪問可能なノードがない場合は終了
        if current == -1:
            break

        visited[current] = True

        # 選択したノードを経由して、未訪問の隣接ノードへの距離を更新（緩和処理）
        for node_no in range(n):
            distance = matrix[current][node_no]
            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    paths[node_no] = paths[current] + [node_no]

    # 出力対象ノードの設定
    targets = [target_node] if target_node is not None else list(range(n))

    for node_no in targets:
        if node_no == start_node or distances[node_no] == INF:
            continue

        path_str = " -> ".join(map(str, paths[node_no]))
        print(f"\n{start_node}-{node_no} distance: {distances[node_no]}\nPath: {path_str}")

    return distances, paths


# === 実行部分 ===
if __name__ == "__main__":
    shortest_path(adj_matrix, 0, 5)
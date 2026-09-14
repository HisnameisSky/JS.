def dfs_n_queens(n: int) -> list[list[str]]:
    results = []
    cols = set()
    diag1 = set()  # row - col (左上から右下の斜め)
    diag2 = set()  # row + col (右上から左下の斜め)

    def dfs(row: int, current_board: list[int]):
        if row == n:
            # 各行のクイーンの位置(col)をもとに 'Q' と '.' の文字列を生成
            board_representation = [
                "." * col + "Q" + "." * (n - col - 1) for col in current_board
            ]
            results.append(board_representation)
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # クイーンの配置（集合に追加）
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            current_board.append(col)

            # 次の行の探索へ
            dfs(row + 1, current_board)

            # バックトラッキング（元の状態に戻す）
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            current_board.pop()

    dfs(0, [])
    return results


# 実行例 (4-Queens)
if __name__ == "__main__":
    solutions = dfs_n_queens(4)
    print(f"解の数: {len(solutions)}")
    for i, sol in enumerate(solutions, 1):
        print(f"\n--- 解 {i} ---")
        for row in sol:
            print(row)
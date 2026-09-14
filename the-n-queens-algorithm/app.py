def dfs_n_queens(n: int) -> list:
    # 1未満の場合は空のリストを返す
    if n < 1:
        return []

    result = []

    def is_valid(board: list, row: int, col: int) -> bool:
        """現在の位置 (row, col) にクイーンを置けるかチェック"""
        for prev_row in range(row):
            prev_col = board[prev_row]
            # 同一列チェック、または斜め射線チェック (|列の差| == 行の差)
            if prev_col == col or abs(prev_col - col) == row - prev_row:
                return False
        return True

    def backtrack(board: list, row: int):
        """深さ優先探索（DFS）とバックトラッキング"""
        # ベースケース: 全ての行 (0 ～ n-1) に配置完了JavaScript で作成された `dfsNQueens` 関数のコードが提示されていませんでしたので、一般的な N-Queens 問題を DFS（深さ優先探索）で解く標準的なコードを用意し、JavaScript から Python へ翻訳いたしました。

### 処理のポイント
* **再帰処理 (DFS):** 各行（`row`）ごとにクイーンを1つずつ配置していきます。
* **衝突判定 (バックトラッキング):** 既存のクイーンの位置（列 `cols`、斜め `diag1`, `diag2`）を集合（`set`）で管理することで、$O(1)$ の高速な判定を行っています。

---

### 1. JavaScript コード（移植元想定）

```javascript
function dfsNQueens(n) {
  const results = [];
  const cols = new Set();
  const diag1 = new Set(); // row - col
  const diag2 = new Set(); // row + col

  function dfs(row, currentBoard) {
    if (row === n) {
      // 盤面を文字列の配列に整形して結果に追加
      results.push(currentBoard.map(col => '.'.repeat(col) + 'Q' + '.'.repeat(n - col - 1)));
      return;
    }

    for (let col = 0; col < n; col++) {
      if (cols.has(col) || diag1.has(row - col) || diag2.has(row + col)) {
        continue;
      }

      // クイーンの配置
      cols.add(col);
      diag1.add(row - col);
      diag2.add(row + col);
      currentBoard.push(col);

      // 次の行へ
      dfs(row + 1, currentBoard);

      // 状態の戻し（バックトラッキング）
      cols.delete(col);
      diag1.delete(row - col);
      diag2.delete(row + col);
      currentBoard.pop();
    }
  }

  dfs(0, []);
  return results;
}
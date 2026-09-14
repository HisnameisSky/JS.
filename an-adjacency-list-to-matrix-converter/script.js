function adjacencyListToMatrix(adjList) {
  // ノード数（オブジェクトのキーの数）を取得
  const numNodes = Object.keys(adjList).length;

  // numNodes x numNodes の 2次元配列（0初期化）を生成
  const matrix = Array.from({ length: numNodes }, () => new Array(numNodes).fill(0));

  // 隣接リストをループ処理して行列に 1 を設定
  for (const node in adjList) {
    const row = Number(node);
    const neighbors = adjList[node];

    for (const neighbor of neighbors) {
      matrix[row][neighbor] = 1;
    }
  }

  // 行列の各行を出力
  for (const row of matrix) {
    console.log(row);
  }

  return matrix;
}
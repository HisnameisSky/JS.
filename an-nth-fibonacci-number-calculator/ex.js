/*メモ化（Top-Down）
【DP: メモ化】一度求めた答えは memo に保存する*/
function fibMemo(n, memo = {}) {
  if (n in memo) return memo[n];
  if (n <= 2) return 1;

  memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
  return memo[n];
}

console.log(fibMemo(50)); // 一瞬で 12586269025 が出る！

/*テーブル化（Bottom-Up）
// 【DP: テーブル化】小さい順に配列を埋めていく*/

function fibTable(n) {
  if (n <= 2) return 1;
  
  const dp = new Array(n + 1).fill(0);
  dp[1] = 1;
  dp[2] = 1;

  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}

console.log(fibTable(50)); // これも一瞬！

//

function climbStairs(n){
    if(n<=2) return n;
    const dp = new Array(n+1).fill(0);
    dp[1]=1;
    dp[2]=2;
    for(let i=3;i<=n;i++){
        dp[i]=dp[i-1]+dp[i=2];
    }
    return dp[n];
}
console.lof(climbStairs(3));
console.log(climbStairs(5));

//

function knapsack(weights,values,capacity){
    const n=weights.length;
    const dp=Array.from({length: n+1},()=> new Array(capacity+1).fill(0));

    for (let i=1; i<=n; i++){
        const weight = weights[i-1];
        const value = values[i-1];

        for (let w = 0; w <= capacity; w++) {
                if(weight <= w){
                dp[i]=Math.max(dp[i-1][w],value + dp[i-1][w-weight]);
            }else{
                dp[i][w]=d[i-1][w];
            }
        }
    }
    return dp[n][capacity];
}
const weights = [2,1,3,2];
const values = [3,2,6,1];
const capacity = 5;
console.log(knapsack(weights, values, capacity));
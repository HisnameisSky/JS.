"""階段登り問題 (Climbing Stairs)"""

def climb_stairs(n:int)->int:
    if n<=2:
        return n

    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2

    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

if __name__ == "__main__":
    print(climb_stairs(3))
    print(climb_stairs(5))

"""0/1 ナップサック問題 (0/1 Knapsack Problem)"""

def knapsack(weights:list, values:list, capacity:int)->int:
    n=len(weights)
    dp=[[0]*(capacity+1)for _ in range(n+1)]

    for i in range(1,n+1):
        weight = weights[i-1]
        value=values[i-1]

        for w in range(capacity+1):
            if weight <= w:
                dp[i][w]=max(dp[i-1][w],value+dp[i-1][w-weight])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][capacity]

if __name__ == "__main__":
    weights = [2,1,3,2]
    values=[3,2,6,1]
    capacity=5
    print(knapsack(weights,values,capacity))


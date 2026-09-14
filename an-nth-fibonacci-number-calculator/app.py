def fibonacci(n:int)->int:
    sequence=[0,1]

    if n ==0:
        return 0
    if n==1:
        return 1

    for i in range(2,n+1):
        next_num = sequence[i-1]+sequence[i-1]
        sequence.append(next_num)
    return sequence[n]

if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(1))   # 1
    print(fibonacci(5))   # 5
    print(fibonacci(10))  # 55
    print(fibonacci(15))  
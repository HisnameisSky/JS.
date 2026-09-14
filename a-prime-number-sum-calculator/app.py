import math
def sum_primes(num:int)->bool:
    if num <2:
        return 0

    def is_prime(n:int)->bool:
        if n <2:
            return False

        for i in range(2, math.isqrt(n)+1):
            if n%i==0:
                return False
        return True
    return sum(i for i in range(2,num+1) if is_prime(i))

if __name__ == "__main__":
    print(sum_primes(10))
    print(sum_primes(5))    # 10 (2 + 3 + 5)
    print(sum_primes(2))    # 2
    print(sum_primes(0))    # 0
    print(sum_primes(977))  # 73156
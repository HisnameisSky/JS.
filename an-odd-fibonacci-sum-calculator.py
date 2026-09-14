def sun_fibs(num):
    prev, curr = 0,1
    total_sum = 0
    while curr <= num:
        if curr % 2 != 0:
            total_sum += curr
        prev, curr = curr, prev + curr
    return total_sum
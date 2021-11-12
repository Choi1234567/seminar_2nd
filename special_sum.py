def calculate_special_sum(n):
    ans = 0
    for a in range(1, n):
        ans += (a ** 2) * (a+1)
    return ans


assert calculate_special_sum(3) == 14

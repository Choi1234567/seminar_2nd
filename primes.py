def is_prime(n, prime_list):
    for i in prime_list:
        if i > n ** 0.5:
            return True
        if n % i == 0:
            return False
    return True


def get_primes(n):
    ans = []
    for i in range(2, n+1):
        if is_prime(i, ans):
            ans.append(i)
    return ans


assert [2, 3, 5, 7, 11] == sorted(get_primes(11))

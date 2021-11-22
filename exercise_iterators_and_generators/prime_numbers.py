from math import sqrt, floor


def get_primes(*args):
    list_primes = []
    not_prime = False
    for i in args[0]:
        if i < 2:
            continue
        boundary = floor(sqrt(i))
        for num in range(2, boundary + 1):
            if i % num == 0:
                not_prime = True
                break
        if not not_prime:
            yield i
        not_prime = False


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))

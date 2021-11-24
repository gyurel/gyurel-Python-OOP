def cache(func):
    log = {}

    def wrapper(n):
        if n in log:
            return log[n]

        current_fib_num = func(n)
        log[n] = current_fib_num

        return current_fib_num

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)

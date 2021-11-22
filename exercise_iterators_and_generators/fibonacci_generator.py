def fibonacci():
    fib_1 = 0
    yield fib_1
    fib_2 = 1
    yield fib_2
    while True:
        next_fib = fib_1 + fib_2
        yield next_fib
        fib_1, fib_2 = fib_2, next_fib


generator = fibonacci()
for i in range(100):
    print(next(generator))

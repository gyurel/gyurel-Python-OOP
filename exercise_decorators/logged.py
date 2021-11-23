def logged(func):
    def wrapper(*args):
        result = f"you called {func.__name__}{args}\nit returned {func(*args)}"
        return result

    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

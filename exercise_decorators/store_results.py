class store_results:
    def __init__(self, func):
        self.func = func
        self.result_list = []

    def __call__(self, *args):
        result = f"Function '{self.func.__name__}' was called. Result: {self.func(*args)}"
        with open('results.txt', 'a') as file:
            file.write(result)
            file.write('\n')


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)

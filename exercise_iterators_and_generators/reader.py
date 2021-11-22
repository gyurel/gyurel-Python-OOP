def read_next(*args):
    for arg in args:
        arg = list(arg)
        for el in arg:
            yield el


for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')

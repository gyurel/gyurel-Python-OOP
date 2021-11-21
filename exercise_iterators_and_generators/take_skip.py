class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_num = -self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 1:
            raise StopIteration
        self.count -= 1
        self.current_num += self.step
        return self.current_num


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

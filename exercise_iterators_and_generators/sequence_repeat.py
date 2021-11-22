class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = list(sequence)
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.number - 1:
            raise StopIteration
        current_index = self.counter % len(self.sequence)
        current_el = self.sequence[current_index]
        self.counter += 1
        return current_el


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
print()
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')

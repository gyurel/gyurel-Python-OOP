class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > len(self.dictionary) - 1:
            raise StopIteration
        current_el = self.dictionary[self.current_index]
        self.current_index += 1
        return current_el


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

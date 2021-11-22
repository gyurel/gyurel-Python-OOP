def solution():

    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            i /= 2
            yield i

    def take(n, seq):
        list_of_halves = []
        for i in range(n):
            current_half_int = next(seq)
            list_of_halves.append(current_half_int)
        return list_of_halves

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))

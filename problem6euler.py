def sumofsquares(x):
    return sum([i ** 2 for i in range(1, x + 1)])


def squareofsum(y):
    return sum(range(1, y + 1)) ** 2


print squareofsum(100) - sumofsquares(100)


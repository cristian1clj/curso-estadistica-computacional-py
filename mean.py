# Python
from random import randint


def find_mean(X: list) -> int:
    return sum(X) / len(X)


def run():
    X = [randint(1, 21) for _ in range(20)]
    print(X)
    
    mean = find_mean(X)
    print(f'Media: {mean}')


if __name__ == '__main__':
    run()
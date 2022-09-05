# Python
from math import sqrt
from random import randint


def find_mean(X: list) -> int:
    return sum(X) / len(X)


def find_variace(X: list, mean: int) -> int:
    aux: int = 0
    
    for element in X:
        aux += (element - mean)**2
        
    return aux / len(X)


def find_strd_deviation(variance: int) -> int:
    return sqrt(variance)


def run():
    X = [randint(1, 21) for _ in range(20)]
    print(X)
    
    mean = find_mean(X)
    print(f'Media: {mean}')
    
    variance = find_variace(X, mean)
    print(f'Varianza: {variance}')
    
    strd_deviation = find_strd_deviation(variance)
    print(f'Desviacion estandar: {strd_deviation}')


if __name__ == '__main__':
    run()
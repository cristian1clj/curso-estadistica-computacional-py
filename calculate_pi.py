# Python
from random import random, choice
from math import sqrt
from typing import List, Tuple

# Files
from statistics import find_strd_deviation, find_mean, find_variace


def throw_needles(needles_amount: int) -> float:
    inside_circle: int = 0
    
    for _ in range(needles_amount):
        x: float = random() * choice([1, -1])
        y: float = random() * choice([1, -1])
        distance_from_center: float = sqrt(x**2 + y**2)
        
        if distance_from_center <= 1:
            inside_circle += 1
    
    return (4 * inside_circle) / needles_amount


def estimate_pi(attempts: int, needles_amount: int) -> Tuple:
    results: List = []
    
    for _ in range(attempts):
        result = throw_needles(needles_amount)
        results.append(result)
    
    mean_results = find_mean(results)
    variance = find_variace(results, mean_results)
    sigma = find_strd_deviation(variance)
    print(f'PI = {round(mean_results, 5)}, Sigma = {sigma}, attempts = {attempts}')
    
    return (mean_results, sigma)


def run(precision: float, attempts: int):
    needles: int = 1000
    sigma = precision
    
    while sigma >= precision / 1.96:
        mean, sigma = estimate_pi(attempts, needles)
        needles *= 2


if __name__ == '__main__':
    run(0.01, 1000)
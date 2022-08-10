
# Fibonacci generator with recusive method (less efficiently)
def recursive_fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


# Fibonacci generator with dinamic method (more efficiently)
def dinamic_fibonacci(n: int, memo: dict) -> int:
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        result = dinamic_fibonacci(n - 1, memo) + dinamic_fibonacci(n - 2, memo)
        memo[n] = result
        
        return result


def run():
    num = int(input("Fibonacci of the number: "))
    result = dinamic_fibonacci(num, {})
    print(result)


if __name__ == '__main__':
    run()
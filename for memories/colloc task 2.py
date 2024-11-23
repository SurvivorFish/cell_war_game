def f(n: int):
    if n % 10 == 0: return -n
    return f(n - 2 * (n % 10)) + 1


scanner_scanner = int(input())
print(f(scanner_scanner))

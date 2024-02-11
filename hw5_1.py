def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n in cache:
            return cache[n]
        elif n <= 0:
            return 0
        elif n == 1:
            return 1
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci
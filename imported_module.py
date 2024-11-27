def factorial(n):
    """Egy szám faktoriálisát adja vissza."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

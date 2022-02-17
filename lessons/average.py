"""Gots to follow the goat P. Kris!"""


def average(x: list[float]) -> float:
    """Calculate the average of a list."""
    total: float = 0.0
    i: int = 0
    while i < len(x):
        total += x[i]
        i += 1
    return total
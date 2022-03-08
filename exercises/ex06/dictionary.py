"""A program to exhibit my understanding of dictionaries in python."""

__author__: str = "730398535"


def invert(a: dict[str, str]) -> dict[str, str]:
    """A function that will flip the keys and value of a dict."""
    webster: dict[str, str] = {}
    for key in a:
        webster[a[key]] = key
    return(webster)


def favorite_color(a: dict[str, str]) -> str:
    """A function that returns the color that is inputed the most, or the first if there is a tie."""
    w: dict[str, int] = {}
    for key in a:
        if a[key] not in w:
            a[key] = 1
        else:
            w[key] += 1
    return (str(w))


def count(a: list[str]) -> dict[str, int]:
    """A function that will count."""
    w: dict[str, int] = {}
    for item in a:
        if item not in w:
            w[item] = 1
        else:
            w[item] += 1
    return w


favorite_color({"KJ": "blue", "AJ": "blue"})
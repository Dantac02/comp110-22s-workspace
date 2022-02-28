"""Assignment File for EX05."""
__author__: str = "730398535"


def only_evens(x: list[int]) -> list[int]:
    """This is a function that will only return even intergers of a inputed list."""
    y = list()
    i: int = 0
    while i < len(x):
        if x[i] % 2 == 0:
            y.append(x[i])
            i += 1
        else:
            i += 1
    return(y)


def sub(x: list[int], y: int, z: int) -> list[int]:
    """A function that appends a new list from input list between inputed indexes."""
    if y < 0:
        y = 0
    if z > len(x):
        z = len(x)
    i: int = y
    sub_list = list()
    while i < z:
        sub_list.append(x[i])
        i += 1
    return sub_list


def concat(x: list[int], y: list[int]) -> list[int]:
    """A function that will combine two list of intergers into one list."""
    i: int = 0
    concat_list = list()
    while i < len(x):
        concat_list.append(x[i])
        i += 1
    i = 0
    while i < len(y):
        concat_list.append(y[i])
        i += 1
    return(concat_list)
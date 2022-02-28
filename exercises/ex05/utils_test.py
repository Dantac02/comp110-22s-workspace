"""Test for said file for EX05."""

__author__: str = "730398535"

from utils import only_evens 
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """A test for an empty list."""
    x: list[int] = []
    assert only_evens(x) == []

   
def test_only_evens_02() -> None:
    """A test for a list."""
    x: list[int] = [1, 2, 3]
    assert only_evens(x) == [2]


def test_only_evens_03() -> None:
    """A test for a list."""
    x: list[int] = [2, 4, 6]
    assert only_evens(x) == [2, 4, 6]


def test_sub_empty() -> None:
    """A test for an empty list."""
    x: list[int] = []
    y: int = 0
    z: int = 0
    assert sub(x, y, z) == []


def test_sub_02() -> None:
    """A test for a list."""
    x: list[int] = [1, 2, 3, 4]
    y: int = 1
    z: int = 3
    assert sub(x, y, z) == [2, 3]


def test_sub_03() -> None:
    """A test for a list."""
    x: list[int] = [1, 2, 3, 4]
    y: int = -1
    z: int = 8
    assert sub(x, y, z) == [1, 2, 3, 4]


def test_concat_empty() -> None:
    """A test for an empty list."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_02() -> None:
    """A test for a list."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [9, 8, 7]
    assert concat(x, y) == [1, 2, 3, 9, 8, 7]


def test_concat_03() -> None:
    """A test for a list."""
    x: list[int] = [1]
    y: list[int] = [2, 3, 4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]
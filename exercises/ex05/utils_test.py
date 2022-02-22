"""Test for said file for EX05."""
__author__: str = "730398535"

from utils import only_evens 
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    x: list[int] = []
    assert only_evens(x) == ()


"""A file to test my functions for dictionaries in python."""
__author__: str = "730398535"

from dictionary import invert
from dictionary import count
from dictionary import favorite_color


def test_invert_01() -> None:
    """A test for an edge case."""
    x: dict[str, str] = {'Conner': 'Mid', 'Evertt': 'Godly', 'Graham': 'Mid'}
    assert invert(x) == {'Mid': 'Graham', 'Godly': 'Evertt'}


def test_invert_02() -> None:
    """The first use case test."""
    x: dict[str, str] = {'UNC': 'Exhausting', 'Duke': 'Overrated', 'NCSU': 'Country'}
    assert invert(x) == {'Exhausting': 'UNC', 'Overated': 'Duke', 'Country': 'NCSU'}


def test_invert_03() -> None:
    """The second use case test."""
    x: dict[str, str] = {'NC': 'Carolina', 'SC': 'Other', 'MC': 'Exsisting?'}
    assert invert(x) == {'Carolina': 'NC', 'Other': 'SC', 'Exsisting': 'MC'}


def test_favorite_color_01() -> None:
    """A test for an edge case."""
    x: dict[str, str] = {'Kevin': 'Carolina Blue', 'Todd': 'Teary Blue', 'Mccombs': 'Teary Blue', 'Rasmey': 'Carolina Blue'}
    assert favorite_color(x) == str == "Carolina Blue"


def test_favorite_color_02() -> None:
    """Second test for a use case."""
    x: dict[str, str] = {'Kevin': 'Red', 'Bob': 'Red', 'Kris': 'Green'}
    assert favorite_color(x) == str == "Red"


def test_favortite_color_03() -> None:
    """Third test for a use case."""
    x: dict[str, str] = {'Evans': 'Eco Blue'}
    assert favorite_color(x) == str == "Eco Blue"


def test_count_01() -> None:
    """A test for a use case."""
    x: list[str] = ["Apple", "Apple", "Banna", "Orange", "Pear"]
    assert count(x) == {'Apple': '2', 'Banna': '1', 'Orange': '1', 'Pear': '1'}


def test_count_02() -> None:
    """A test for a use case."""
    x: list[str] = ["Apple", "Banna", "Orange", "Pear", "Orange"]
    assert count(x) == {'Apple': '1', 'Banna': '1', 'Orange': '2', 'Pear': '1'}


def test_count_03() -> None:
    """A test for an edge case."""
    x: list[str] = []
    assert count(x) == {}

"""testing if i really know what I am doing."""

from lessons.average import average


def test_average_empty() -> None:
    x: list[float] = []
    assert average(x) == 0.0


def test_average_single_item() -> None:
    x: list[float] = [110.0]
    assert average(x) == 110.0


def test_average_many_items() -> None:
    x: list[float] = [2.0, 4.0, 6.0, 8.0, 10.0]
    assert average(x) == 30.0


def test_average_many_items_again() -> None:
    assert average([4.0, 8.0, 12.0, 16.0, 20.0]) == 60.0

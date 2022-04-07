"""Dictionary related utility functions."""

__author__ = "730398535"
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Writes the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    cvs_reader = DictReader(file_handle)
    for row in cvs_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Generates a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Mutates a row orientated table into a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], range: int) -> dict[str, list[str]]:
    """A function that produces a new column-based dict within a set range."""
    result: dict[str, list[str]] = {}
    if range > len(table):
        range = len(table)
    for key in table:
        new_list: list[str] = []
        i: int = 0
        while i < range:
            new_list.append(table[key][i])
            i += 1
        result[key] = new_list
    return result


def select(table: dict[str, list[str]], subset: list[str]) -> dict[str, list[str]]:
    """Function that returns a new dict based on og dict and subset list."""
    result: dict[str, list[str]] = {}
    for key in subset:
        result[key] = table[key]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces new dict from two combinded og dicts."""
    result: dict[str, list[str]] = {}
    for key in table_one:
        result[key] = table_one[key]
    for key in table_two:
        if table_two.keys == result.keys:
            result[key] = table_two[key]
        else:
            table_two[key] = result[key]
    return result


def count(a: list[str]) -> dict[str, int]:
    """A function that will count how many times a value appeard."""
    result: dict[str, int] = {}
    for item in a:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result

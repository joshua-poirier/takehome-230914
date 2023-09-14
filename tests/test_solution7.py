import pytest

from takehome.solutions.solution7 import number_of_employees


@pytest.mark.parametrize("number_of_characters, expected", [(15, 12), (2040, 716)])
def test_number_of_employees(number_of_characters: int, expected: int) -> None:
    actual = number_of_employees(number_of_digits=number_of_characters)

    assert actual == expected

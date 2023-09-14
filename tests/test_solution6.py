import pytest

from takehome.solutions.solution6 import limiter


@pytest.mark.parametrize("input, expected", [(5, 9), (3, 81)])
def test_given_cases(input: int, expected: int) -> None:
    actual = limiter(n=input)

    assert actual == expected

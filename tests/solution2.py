import pytest

from takehome.solutions.solution2 import minimal_number_of_packages


@pytest.mark.parametrize(
    "items, available_large_packages, available_small_packages, expected",
    [
        pytest.param(16, 2, 10, 8, id="base test given by company"),
        pytest.param(4, 2, 10, 4, id="using only small packages"),
        pytest.param(5, 2, 10, 1, id="using only large packages"),
    ],
)
def test_sufficient_packages(
    items: int,
    available_large_packages: int,
    available_small_packages: int,
    expected: int,
) -> None:
    """Happy path testing
    """
    actual = minimal_number_of_packages(
        items=items,
        available_large_packages=available_large_packages,
        available_small_packages=available_small_packages,
    )

    assert actual == expected


@pytest.mark.parametrize(
    "items, available_large_packages, available_small_packages",
    [
        pytest.param(16, 0, 10, id="No large packages, insufficient small packages"),
        pytest.param(16, 5, 0, id="No small packages, insufficient large packages"),
        pytest.param(16, 0, 0, id="No small or large packages"),
        pytest.param(16, -1, -1, id="Negative packages available"),
    ],
)
def test_too_few_packages(
    items: int,
    available_large_packages: int,
    available_small_packages: int,
) -> None:
    """Sad path testing
    """
    actual = minimal_number_of_packages(
        items=items,
        available_large_packages=available_large_packages,
        available_small_packages=available_small_packages,
    )

    assert actual == -1

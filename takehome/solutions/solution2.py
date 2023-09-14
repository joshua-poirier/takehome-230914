LARGE_CAPACITY: int = 5
SMALL_CAPACITY: int = 1


def solution2() -> None:
    """Interface I can iterate on quickly before copying the solution to the employer.
    """
    answer = minimal_number_of_packages(16, 2, 10)
    print(answer)


def minimal_number_of_packages(
    items: int,
    available_large_packages: int = LARGE_CAPACITY,
    available_small_packages: int = SMALL_CAPACITY,
) -> int:
    """Calculate the minimum number of packages needed to hold a given number of items.

    Args:
        items (int): Number of items needed to be packaged.
        available_large_packages (int): Available number of large packages.
        available_small_packages (int): Available number of small packages.

    Returns:
        Minimum number of packages needed to hold the given number of items.
    """
    # calculate the number of large, small, and total packages to be used
    n_large = min(items // LARGE_CAPACITY, available_large_packages)
    n_small = min(items - (n_large * LARGE_CAPACITY), available_small_packages)
    n_packages = (n_large * LARGE_CAPACITY) + (n_small * SMALL_CAPACITY)

    if n_packages < items:
        # not enough packages to package all items
        return -1
    else:
        return n_large + n_small

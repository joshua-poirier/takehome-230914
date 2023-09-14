MAX_CHARACTERS: int = 2147483647


def solution7() -> None:
    print(number_of_employees(2040))


def number_of_employees(number_of_digits: int) -> int:
    """Calculate the number of employees given the number of digits it takes to assign
    each an ID.

    Args:
        number_of_digits (int): The number of digits required to assign each employee
            an ID.

    Returns:
        int: Number of employees given the number of digits it takes to assign each an
            ID.
    """
    # initialize the running total
    running_total: int = 0

    # iterate through employee ID numbers, calculating the total number of characters
    for i in range(1, MAX_CHARACTERS):
        running_total += len(str(i))
        if running_total >= number_of_digits:
            return i

    return 0

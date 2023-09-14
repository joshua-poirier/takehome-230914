def solution6() -> None:
    print(limiter(5))
    print(limiter(3))


def limiter(n: int) -> int:
    """Understanding the behavior of a recursive function.

    Args:
        n (int): An input number.

    Returns:
        A recursively manipulated integer based on the input.
    """
    if n == 6:
        return 3
    else:
        return 3 * limiter(n + 1)

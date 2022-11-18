from typing import TypeVar, Optional, Callable, Sequence

T = TypeVar("T")


def find_middle(left: int, right: int):
    return (left + right) // 2


def check_near(left: int, right: int):
    return right - left > 1


def check(value1, value2, key):
    return key(value1) < key(value2)


def binary_search(
        arr: Sequence[T],
        need_value: int,
        *,
        key: Callable = (lambda _: _),
        left: Optional[int] = None,
        right: Optional[int] = None
) -> int:
    if left is None:
        left = -1
    if right is None:
        right = len(arr)

    if left > right:
        raise ValueError()

    while check_near(left, right):
        middle = find_middle(left, right)
        if check(arr[middle], need_value, key):
            left = middle
        else:
            right = middle

    return right

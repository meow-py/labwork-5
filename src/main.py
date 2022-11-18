from typing import TypeVar, Optional, Callable, Sequence


def find_middle(left: int, right: int):
    return (left + right) // 2


def check_near(left: int, right: int):
    return right - left > 1


def check(value1, value2, key):
    return key(value1) < key(value2)


def binary_search(
        func: Callable,
        left: int,
        right: int,
) -> int:

    if left > right:
        raise ValueError()

    while check_near(left, right):
        middle = find_middle(left, right)
        if func(middle):
            left = middle
        else:
            right = middle

    return right


def array_binary_search(
        arr: Sequence,
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

    def array_search(i):
        return check(arr[i], need_value, key)

    return binary_search(array_search, left, right)

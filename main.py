from typing import TypeVar, Optional, Callable, Sequence

T = TypeVar("T")


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

    while right - left > 1:
        middle = (left + right) // 2
        if key(arr[middle]) < key(need_value):
            left = middle
        else:
            right = middle

    return right

def standardCMP(current_value):
    return current_value


def binarySearch(arr: list, need_value, cmp=standardCMP, left=None, right=None):
    if left is None:
        left = -1
    if right is None:
        right = len(arr)

    if left > right:
        return False

    while right - left > 1:
        middle = (left + right) // 2
        if cmp(arr[middle]) > cmp(need_value):
            right = middle
        else:
            left = middle
    return right if right < len(arr) and cmp(arr[right]) == cmp(need_value) else (left if left >= 0 and cmp(arr[left]) == cmp(need_value) else -1)


def main():
    for i in range(0, 10):
        arr = [i for i in range(1, 9)]
        print(arr, i, binarySearch(arr, i))


if __name__ == '__main__':
    main()
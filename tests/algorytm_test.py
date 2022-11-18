from main import *


def test_example():
    arr = [i for i in range(0, 9)]
    for i in range(0, 10):
        assert i == array_binary_search(arr, i)


def test_with_array():
    arr = [i for i in range(0, 9)]
    for i in range(0, 10):
        assert i == array_binary_search(arr, i)


def test_not_in_array_right():
    arr = [i for i in range(0, 9)]
    for i in [100, 10]:
        assert 9 == array_binary_search(arr, i)


def test_not_in_array_left():
    arr = [i for i in range(0, 9)]
    for i in [-100, -10]:
        assert 0 == array_binary_search(arr, i)


def test_find_middle():
    for a in range(100):
        for b in range(100):
            assert find_middle(a, b) == (a + b) // 2


def test_check_near():
    assert not check_near(5, 6)
    assert check_near(1, 100)


def test_check():
    for value1 in range(100):
        for value2 in range(100):
            assert check(value1, value2, lambda x: x) == (value1 < value2)


def test_cows():
    arr = [0, 10, 15, 25, 100]
    for (k, ans) in [(2, 100), (3, 25), (4, 10), (5, 5)]:
        assert (arr, )
from main import binary_search


def test_example():
    arr = [i for i in range(0, 9)]
    for i in range(0, 10):
        assert i == binary_search(arr, i)


def test_not_in_array_right():
    arr = [i for i in range(0, 9)]
    for i in [100, 10]:
        assert 9 == binary_search(arr, i)


def test_not_in_array_left():
    arr = [i for i in range(0, 9)]
    for i in [-100, -10]:
        assert 0 == binary_search(arr, i)
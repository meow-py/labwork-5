from main import binary_search


def test_example():
    arr = [i for i in range(0, 9)]
    for i in range(0, 10):
        assert i == binary_search(arr, i)

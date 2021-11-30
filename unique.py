from collections import Counter


def compress(lst):
    counter = Counter()
    ans = []
    for i in lst:
        counter.update([i])
    for j in counter.items():
        ans.append(j)
    return ans


if __name__ == '__main__':
    expected_sorted = [(1, 2), (2, 1), (3, 1)]
    actual_sorted = sorted(compress([1, 2, 1, 3]))
    assert expected_sorted == actual_sorted

"""Count index pairs i < j whose absolute difference is k."""
import sys
from collections import Counter


def count_pairs(values, k):
    """Return the number of distinct index pairs with |a[i]-a[j]| == k."""
    frequencies = Counter(values)
    difference = abs(k)
    if difference == 0:
        return sum(count * (count - 1) // 2 for count in frequencies.values())
    return sum(count * frequencies.get(value + difference, 0)
               for value, count in frequencies.items())


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k = data[0], data[1]
    values = data[2:2 + n]
    print(count_pairs(values, k))


if __name__ == "__main__":
    main()

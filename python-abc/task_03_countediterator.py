#!/usr/bin/python3

class CountedIterator:
    """Iterator that counts the number of items iterated over."""

    def __init__(self, data):
        self._data = data
        self._index = 0
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration
        item = self._data[self._index]
        self._index += 1
        self._count += 1
        return item

    def get_count(self):
        """Return the number of items iterated over."""
        return self._count

# Script demonstrating the use of CountedIterator
data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")

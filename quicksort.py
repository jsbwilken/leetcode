from random import shuffle

import numpy as np


def partition(array: list[int], start: int, end: int):
    center = (start + end) // 2
    pivot = array[center]

    left = start
    right = end
    while True:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left >= right:
            return left

        array[left], array[right] = array[right], array[left]

def quicksort(array: list[int]):

    if len(array) <= 1:
        return

    p = partition(array, 0, len(array) - 1)
    quicksort(array[0:p])
    quicksort(array[p+1:])

nums = list(range(1, 2000))
shuffle(nums)
np_nums = np.array(nums)
np_nums2 = np.array(nums)
np_nums2 = np.sort(np_nums2, axis=None)
quicksort(np_nums)
print(np_nums)

assert np.all(np_nums == np_nums2)



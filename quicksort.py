from random import shuffle

import numpy as np


def partition(array: list[int]):
    pivot = array[-1]

    idx = -1

    for n in range(len(array)-1):
        if array[n] <= pivot:
            idx += 1
            array[idx], array[n] = array[n], array[idx]

    idx += 1
    array[idx], array[-1] = array[-1], array[idx]

    return idx

def quicksort(array: list[int]):

    if len(array) <= 1:
        return

    p = partition(array)
    quicksort(array[0:p])
    quicksort(array[p+1:])

nums = list(range(20))
shuffle(nums)
np_nums = np.array(nums)
np_nums2 = np.array(nums)
np_nums2 = np.sort(np_nums2, axis=None)
quicksort(np_nums)
print(np_nums)

assert np.all(np_nums == np_nums2)



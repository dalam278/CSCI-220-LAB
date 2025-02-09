# Discrete Structures (CSCI 220)
# Winter 2023
# Assignment 4 -
# Didarul Alam

# Acknowledgements:
# I worked with the class
# I used the following sites ... (if applicable)

import math
import random
import time
import pandas as pd
import matplotlib.pyplot as plt


def binary_search_recursive_helper(arr, key, l, r):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search_recursive_helper(arr, key, l, mid - 1)
        else:
            return binary_search_recursive_helper(arr, key, mid + 1, r)
    return -1


def binary_search_recursive(arr, key):
    return binary_search_recursive_helper(arr, key, 0, len(arr) - 1)


def binary_search_iterative(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + int((r - l) / 2)
        if arr[m] == key:
            return m
        elif arr[m] < key:
            l = m + 1
        else:
            r = m - 1
    return -1


def binary_search_better(arr, key):
    l, r = 0, len(arr) - 1
    while r - l > 1:
        m = l + (r - l) // 2
        if arr[m] <= key:
            l = m
        else:
            r = m
    if arr[l] == key:
        return l
    if arr[r] == key:
        return r
    return -1


def binary_search_randomized_helper(arr, key, l, r):
    if r >= l:
        mid = random.randint(l, r)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search_randomized_helper(arr, key, l, mid - 1)
        return binary_search_randomized_helper(arr, key, mid + 1, r)
    return -1


def binary_search_randomized(arr, key):
    return binary_search_randomized_helper(arr, key, 0, len(arr) - 1)


def random_sorted_list(size):
    my_list = []
    prev = 0
    for i in range(size):
        curr = prev + random.randint(1, 10)
        my_list.append(curr)
        prev = curr
    return my_list


def native_search(arr, key):
    return arr.index(key)


def linear_search_iterative(arr, key):
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i
    return -1


def exponential_search(arr, key):
    if arr[0] == key:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= key:
        i = i * 2
    return binary_search_recursive_helper(arr, key, int(i / 2), min(i, n - 1))


# def linear_search_recursive(arr, key):
#     return linear_search_recursive_helper(arr, key, 0)


# def linear_search_recursive_helper(arr, key, i):
#     if i >= len(arr):
#         return -1
#     elif arr[i] == key:
#         return i
#     else:
#         return linear_search_recursive_helper(arr, key, i + 1)


def run_algs(algs, sizes, trials):
    dict_algs = {}
    for alg in algs:
        dict_algs[alg.__name__] = {}
    for size in sizes:
        for alg in algs:
            dict_algs[alg.__name__][size] = 0
        for trial in range(1, trials + 1):
            arr = random_sorted_list(size)
            idx = random.randint(0, size - 1)
            key = arr[idx]
            for alg in algs:
                start_time = time.time()
                idx_found = alg(arr, key)
                end_time = time.time()
                if idx_found != idx:
                    print(alg.__name__, "wrong index found", arr, idx, idx_found)
                net_time = end_time - start_time
                dict_algs[alg.__name__][size] += 1000 * net_time
    return dict_algs


def jump_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[int(prev)] < key:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == key:
        return prev
    return -1


def fibonacci_search(arr, key):
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
    offset = -1
    while fib > 1:
        i = min(offset + fib2, n - 1)
        if arr[i] < key:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > key:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and arr[n - 1] == key:
        return n - 1
    return -1


def interpolation_search_helper(arr, key, lo, hi):
    if arr[lo] == arr[hi]:
        if key == arr[lo]:
            return lo
        else:
            return -1
    if lo <= hi and arr[lo] <= key <= arr[hi]:
        pos = int(lo + ((hi - lo) / float(arr[hi] - arr[lo]) * float(key - arr[lo])))
        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            return interpolation_search_helper(arr, key, pos + 1, hi)
        else:
            return interpolation_search_helper(arr, key, lo, pos - 1)
    return -1


def interpolation_search(arr, key):
    return interpolation_search_helper(arr, key, 0, len(arr) - 1)


def ternary_search_helper(arr, key, l, r):
    if r >= l:
        third = int((r - l) / 3)
        mid1 = l + third
        mid2 = r - third
        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif key < arr[mid1]:
            return ternary_search_helper(arr, key, l, mid1 - 1)
        elif key > arr[mid2]:
            return ternary_search_helper(arr, key, mid2 + 1, r)
        else:
            return ternary_search_helper(arr, key, mid1 + 1, mid2 - 1)
    return -1


def ternary_search(arr, key):
    return ternary_search_helper(arr, key, 0, len(arr) - 1)


def print_times(dict_algs):
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)
    df = pd.DataFrame.from_dict(dict_algs).T
    print(df)


def plot_times(dict_algs, sizes, trials, algs, title, file_name):
    alg_num = 0
    plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])
    for alg in algs:
        alg_num += 1
        d = dict_algs[alg.__name__]
        x_axis = [j + 0.05 * alg_num for j in range(len(sizes))]
        y_axis = [d[i] for i in sizes]
        plt.bar(x_axis, y_axis, width=0.05, alpha=0.75, label=alg.__name__)
    plt.legend()
    plt.title(title)
    plt.xlabel("Size")
    plt.ylabel("Time for " + str(trials) + " trials (ms)")
    plt.savefig(file_name)
    plt.show()


def main():
    assn = "Assignment4"
    title = "Runtime of search algorithms"
    sizes = [10, 100, 1000, 10000, 100000]
    searches = [native_search, linear_search_iterative, binary_search_recursive,
                binary_search_iterative, binary_search_better, binary_search_randomized,
                exponential_search, jump_search, fibonacci_search, interpolation_search,
                ternary_search]
    trials = 1000
    dict_searches = run_algs(searches, sizes, trials)
    print_times(dict_searches)
    plot_times(dict_searches, sizes, trials, searches, title, assn + ".png")


if __name__ == "__main__":
    main()

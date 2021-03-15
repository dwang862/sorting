#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input
which controls how the elements of the list
should be compared against each other:
If cmp(a, b) returns -1, then a < b;
if cmp(a, b) returns  1, then a > b;
if cmp(a, b) returns  0, then a == b.
'''

import random
import copy


def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest

    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest

    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.

    NOTE:
    In python, helper functions are frequently prepended with the _.
    This is a signal to users of a library that
    these functions are for "internal use only",
    and not part of the "public interface".

    This _merged function could be implemented as a local function within
    the merge_sorted scope rather than a global function.
    The downside of this is that the
    function can then not be tested on its own.
    Typically, you should only implement a function as a
    local function if it cannot function on its own
    (like the go functions from binary search).
    If it's possible to make a function stand-alone,
    then you probably should do that and write
    test cases for the stand-alone function.

    >>> _merged([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    '''
    x = y = 0
    check_list = []
    while x < len(xs) and y < len(ys):
        check = cmp(xs[x], ys[y])
        if check == -1:
            check_list.append(xs[x])
            x += 1
        if check == 1:
            check_list.append(ys[y])
            y += 1
        if check == 0:
            check_list.append(xs[x])
            check_list.append(ys[y])
            x += 1
            y += 1
    while x < len(xs):
        check_list.append(xs[x])
        x += 1
    while y < len(ys):
        check_list.append(ys[y])
        y += 1
    return check_list


def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    xs_copy = copy.deepcopy(xs)
    if len(xs_copy) <= 1:
        return xs_copy
    else:
        mid = len(xs_copy) // 2
        left = merge_sorted(xs_copy[:mid], cmp)
        right = merge_sorted(xs_copy[mid:], cmp)
        return _merged(left, right, cmp)


def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected,
    and the list is split into a "less than"
    sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            put all the values equal to p in a list
            sort the greater/less than lists recursively
            return the concatenation of (less than, equal, greater than)

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    '''
    xs_copy = copy.deepcopy(xs)
    '''
    xs_copy = copy.deepcopy(xs)
    if len(xs_copy) <= 1:
        return xs_copy
    else:
        pivot = random.randint(0, len(xs_copy) - 1)
        less = []
        equal = []
        greater = []
        for i in xs_copy:
            var = cmp(i, xs_copy[pivot])
            if var == -1:
                less.append(i)
            elif var == 0:
                equal.append(i)
            elif var == 1:
                greater.append(i)
        return quick_sorted(less, cmp) + equal + quick_sorted(greater, cmp)


def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented "in-place".
    This means that no extra lists are allocated,
    or that the algorithm uses Theta(1) additional memory.
    Merge sort, on the other hand, must allocate
    intermediate lists for the merge step,
    and has a Theta(n) memory requirement.
    Even though quick sort and merge sort both
    have the same Theta(n log n) runtime,
    this more efficient memory usage typically
    makes quick sort faster in practice.
    (We say quick sort has a lower "constant factor" in its runtime.)
    The downside of implementing quick sort in this way is that
    it will no longer be a [stable sort]
    (https://en.wikipedia.org/wiki/Sorting_algorithm#Stability),
    but this is typically inconsequential.

    Follow the pseudocode of the Lomuto partition scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    You should directly modify the input xs
    variable instead of returning a copy of the list.
    '''

#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    result = []
    left = 0
    right = 0
    
    # TODO: Repeat until one list is empty
    while left < len(items1) and right < len(items2):
    # TODO: Find minimum item in both lists and append it to new list
        if items1[left] < items2[right]:
            result.append(items1[left])
            left += 1
    # TODO: Append remaining items in non-empty list to new list
        else:
            result.append(items2[right])
            right += 1
    while left < len(items1):
        result.append(items1[left])
        left += 1
    while right < len(items2):
        result.append(items2[right])
        right += 1

    return result


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    mid = len(items) // 2
    # TODO: Sort each half using any other sorting algorithm
    left = items[:mid]
    right = items[mid:]
    # TODO: Merge sorted halves into one list in sorted order
    
    return left, right


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    # TODO: Split items list into approximately equal halves
    left_half, right_half = split_sort_merge(items)
    # TODO: Sort each half by recursively calling merge sort
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    # TODO: Merge sorted halves into one list in sorted order
    return merge(left, right)

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot = items[high]
    i = low - 1

    for j in range(low, high):
        if items[j] <= pivot:
            i = i + 1
            (items[i], items[j]) = (items[j], items[i])

    (items[i + 1], items[high]) = (items[high], items[i + 1])
    return i + 1


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    # if len(items) <= 1:
    #     return items
    # low = []
    # high = []
    # pivot = items[0]
    # for item in items[1:]:
    #     if item <= pivot:
    #         low.append(item)
    #     else:
    #         high.append(item)
    # return quick_sort(low) + [pivot] + quick_sort(high)

    if low < high:
        pi = partition(items, low, high)
        quick_sort(items, low, pi - 1)
        quick_sort(items, pi + 1, high)
    return items

if __name__ == "__main__":
    # alist = [20, 19, 18, 13, 16, 5, 10, 17, 17, 3]
    # l = merge_sort(alist)
    # print(l)

    alist = [3,2,3,6,9,7,5]
    print(quick_sort(alist, 0, len(alist) - 1))
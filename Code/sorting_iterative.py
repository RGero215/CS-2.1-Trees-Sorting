#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) Why and under what conditions?
    TODO: Memory usage: O(1) Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for index in range(len(items) - 1):
        if items[index] > items[index + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) n(n-1) / 2 or (n^2 - n) Why and under what conditions? O(n) best and  O(n^2) worst
    TODO: Memory usage: O(1) Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(items) - 1):
            if items[i] > items[i - 1]:
                items[i], items[i - 1] = items[i -1], items[i]
                swapped = True

    # TODO: Swap adjacent items that are out of order


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2) Why and under what conditions?
    TODO: Memory usage: O(1) Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    sorted_list = []
    print("%-25s %-25s" % (items, sorted_list))
    for i in range(0, len(items)):
        index_to_move = index_of_min(items)
        sorted_list.append(items.pop(index_to_move))
        print("%-25s %-25s" % (items, sorted_list))
    return sorted_list

def index_of_min(items):
    min_index = 0
    for i in range(1, len(items)):
        if items[i] < items[min_index]:
            min_index = i
    return min_index


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2) Why and under what conditions?
    TODO: Memory usage: O(1) Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for step in range(1, len(items)):
        key = items[step]
        j = step - 1
        while j >= 0 and key < items[j]:
            items[j + 1] = items[j]
            j = j - 1
        items[j + 1] = key
    return items


if __name__ == "__main__":
    # unsorted_list = [4,7,8,1]
    # print(selection_sort(unsorted_list))

    unsorted_list = [4,7,8,1]
    print(insertion_sort(unsorted_list))
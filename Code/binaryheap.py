#!python


class BinaryMinHeap(object):
    """BinaryMinHeap: a partially ordered collection with efficient methods to
    insert new items in partial order and to access and remove its minimum item.
    Items are stored in a dynamic array that implicitly represents a complete
    binary tree with root node at index 0 and last leaf node at index n-1."""

    def __init__(self, items=None):
        """Initialize this heap and insert the given items, if any."""
        # Initialize an empty list to store the items
        self.items = []
        if items:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this heap."""
        return 'BinaryMinHeap({})'.format(self.items)

    def is_empty(self):
        """Return True if this heap is empty, or False otherwise."""
        # TODO: Check if empty based on how many items are in the list
        return len(self.items) == 0

    def size(self):
        """Return the number of items in this heap."""
        return len(self.items)

    def insert(self, item):
        """Insert the given item into this heap.
        TODO: Best case running time: O(1), if the item is the largest element
        TODO: Worst case running time: O(log(n)), if the item is the smallest"""
        # Insert the item at the end and bubble up to the root
        self.items.append(item)
        if self.size() > 1:
            self._bubble_up(self._last_index())

    def get_min(self):
        """Return the minimum item at the root of this heap.
        Best and worst case running time: O(1) because min item is the root."""
        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        assert self.size() > 0
        return self.items[0]

    def delete_min(self):
        """Remove and return the minimum item at the root of this heap.
        TODO: Best case running time: O(1), whenever the size of self.items is less than or equal to one
        TODO: Worst case running time: O(log(n) in all other cases"""
        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        elif self.size() == 1:
            # Remove and return the only item
            return self.items.pop()
        assert self.size() > 1
        min_item = self.items[0]
        # Move the last item to the root and bubble down to the leaves
        last_item = self.items.pop()
        self.items[0] = last_item
        if self.size() > 1:
            self._bubble_down(0)
        return min_item

    def replace_min(self, item):
        """Remove and return the minimum item at the root of this heap,
        and insert the given item into this heap.
        This method is more efficient than calling delete_min and then insert.
        TODO: Best case running time: O(1), if the item passed in is less than or equal to the current minimum.
        TODO: Worst case running time: O(log n), if the item is the element"""
        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        assert self.size() > 0
        min_item = self.items[0]
        # Replace the root and bubble down to the leaves
        self.items[0] = item
        if self.size() > 1:
            self._bubble_down(0)
        return min_item

    def _bubble_up(self, index):
        """Ensure the heap ordering property is true above the given index,
        swapping out of order items, or until the root node is reached.
        Best case running time: O(1) if parent item is smaller than this item.
        Worst case running time: O(log n) if items on path up to root node are
        out of order. Maximum path length in complete binary tree is log n."""
        if index == 0:
            return  # This index is the root node (does not have a parent)
        if not (0 <= index <= self._last_index()):
            raise IndexError('Invalid index: {}'.format(index))
        # Get the item's value
        item = self.items[index]
        # Get the parent's index and value
        parent_index = self._parent_index(index)
        parent_item = self.items[parent_index]
        # TODO: Swap this item with parent item if values are out of order
        if item < parent_item:
            self.items[index], self.items[parent_index] = parent_item, item
        # TODO: Recursively bubble up again if necessary
            if parent_index > 0:
                    new_parent_index = self._parent_index(parent_index)
                    if item < self.items[new_parent_index]:
                        self._bubble_up(parent_index)

    def _bubble_down(self, index):
        """Ensure the heap ordering property is true below the given index,
        swapping out of order items, or until a leaf node is reached.
        Best case running time: O(1) if item is smaller than both child items.
        Worst case running time: O(log n) if items on path down to a leaf are
        out of order. Maximum path length in complete binary tree is log n."""
        if not (0 <= index <= self._last_index()):
            raise IndexError('Invalid index: {}'.format(index))
        # Get the index of the item's left and right children
        left_index = self._left_child_index(index)
        right_index = self._right_child_index(index)
        if left_index > self._last_index():
            return  # This index is a leaf node (does not have any children)
        # Get the item's value
        item = self.items[index]
        # TODO: Determine which child item to compare this node's item to
        child_index = left_index
        if right_index <= last:
            if self.items[right_index] < self.items[left_index]:
                child_index = right_index
        # TODO: Swap this item with a child item if values are out of order
        child_item = self.items[child_index]
        # TODO: Recursively bubble down again if necessary
        if item > child_item:
            self.items[index], self.items[child_index] = child_item, item
            return self._bubble_down(child_index)

    def _last_index(self):
        """Return the last valid index in the underlying array of items."""
        return len(self.items) - 1

    def _parent_index(self, index):
        """Return the parent index of the item at the given index."""
        if index <= 0:
            raise IndexError('Heap index {} has no parent index'.format(index))
        return (index - 1) >> 1  # Shift right to divide by 2

    def _left_child_index(self, index):
        """Return the left child index of the item at the given index."""
        return (index << 1) + 1  # Shift left to multiply by 2

    def _right_child_index(self, index):
        """Return the right child index of the item at the given index."""
        return (index << 1) + 2  # Shift left to multiply by 2


def test_binary_min_heap():
    # Create a binary min heap of 7 items
    items = [9, 25, 86, 3, 29, 5, 55]
    heap = BinaryMinHeap()
    print('heap: {}'.format(heap))

    print('\nInserting items:')
    for index, item in enumerate(items):
        heap.insert(item)
        print('insert({})'.format(item))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))
        heap_min = heap.get_min()
        real_min = min(items[: index + 1])
        correct = heap_min == real_min
        print('get_min: {}, correct: {}'.format(heap_min, correct))

    print('\nDeleting items:')
    for item in sorted(items):
        heap_min = heap.delete_min()
        print('delete_min: {}'.format(heap_min))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))

def heapify(arr, n, i): 
    """Time complexity of heapify is O(Logn)"""
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    """time complexity of Heap Sort is O(nLogn)"""
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 


if __name__ == '__main__':
    test_binary_min_heap()

    # Driver code to test above 
    arr = [ 12, 11, 13, 5, 6, 7] 
    heapSort(arr) 
    n = len(arr) 
    print ("Sorted array is") 
    for i in range(n): 
        print ("%d" %arr[i]), 
    # This code is contributed by Mohit Kumra https://www.geeksforgeeks.org/heap-sort/

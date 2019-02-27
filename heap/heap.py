

class Heap:
    """
    A binary tree ordered such that the maximum values contained in the tree
    can be accessed in constant time, and modifications of the tree can be
    performed in logarithmic time.
    """

    def __init__(self):
        self.storage = []

    def insert(self, value):
        """Inserts an item into the correct place in the heap."""
        # Add item to next position in heap
        self.storage.append(value)
        # Reorder according to heap rules
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        """Removes and returns the top item from the heap."""
        # Handle deletion from an empty heap
        if(len(self.storage) is 0):
            return None
        # Remove top of the heap, and last item in heap
        value_high = self.storage[0]
        value_last = self.storage.pop()
        # Place last item on top of the heap, and reorder
        if(len(self.storage)):
            self.storage[0] = value_last
            self._sift_down(0)
        # Return highest item
        return value_high

    def get_max(self):
        """Returns the maximum value stored in the heap."""
        return self.storage[0]

    def get_size(self):
        """Returns the number of items stored in the heap."""
        return len(self.storage)

    def _bubble_up(self, index):
        """
        Moves the element at the specified index "up" the heap by swapping it
        with its parent if the parent's value is less than the value at the
        specified index.
        """
        # Determine the index and value of the current node and its parent
        index_parent = int((index-1)/2)
        value_parent = self.storage[index_parent]
        value_index = self.storage[index]
        # If necessary, swap them and repeat the process recursively
        if(value_parent < value_index):
            self.storage[index_parent] = value_index
            self.storage[index] = value_parent
            self._bubble_up(index_parent)

    def _sift_down(self, index):
        """
        grabs the indices of this element's children and determines which child
        has a larger value. If the larger child's value is larger than the
        parent's value, the child element is swapped with the parent.
        """
        # Determine the value and index of the largest child node at this index
        # Get index and value of first ('left') child, if any
        index_left = index*2 + 1
        if(index_left >= len(self.storage)):
            return
        value_left = self.storage[index_left]
        # Get index and value of second ('right') child, if any
        value_large = value_left
        index_large = index_left
        index_right = index*2 + 2
        if(index_right < len(self.storage)):
            value_right = self.storage[index_right]
            if(value_left < value_right):
                value_large = value_right
                index_large = index_right
        # If necessary, swap the currently indexed no with a larger child node
        # Then repeat the whole process again recursively
        value_test = self.storage[index]
        if(value_test is None or value_test < value_large):
            self.storage[index] = value_large
            self.storage[index_large] = value_test
            self._sift_down(index_large)

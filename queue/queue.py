

class Queue:
    def __init__(self):
        self.size = 0
        # Setup front of queue, back of queue
        self.front = None
        self.back = None

    def enqueue(self, item):
        # Handle linked list creation for first item
        if(self.size is 0):
            self.front = self.Node(item)
            self.back = self.front
            self.size += 1
            return
        # Add item to back of list
        self.back = self.back.link(item)
        self.size += 1

    def dequeue(self):
        # Return None if no values are in the queue
        if(self.size is 0):
            return None
        # Manage linked list structure
        next_value = self.front.value
        self.front = self.front.next
        self.size -= 1
        # Return next value
        return next_value

    def len(self):
        return self.size

    # - Utility Subclasses ---------------------------
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def link(self, next):
            self.next = Queue.Node(next)
            return self.next

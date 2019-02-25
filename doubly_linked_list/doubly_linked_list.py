

class ListNode:
    """
    Each ListNode holds a reference to its previous node as well as its next
    node in the List.
    """
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        """
        Wrap the given value in a ListNode and insert it after this node. Note
        that this node could already have a next node it is point to.
        """
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        """
        Wrap the given value in a ListNode and insert it before this node. Note
        that this node could already have a previous node it is point to.
        """
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        """
        Rearranges this ListNode's previous and next pointers accordingly,
        effectively deleting this ListNode.
        """
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    """
    Our doubly-linked list class. It holds references to the list's head and
    tail nodes.
    """
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        # Handle first insertion (setup head and tail)
        if(self.head is None):
            self.head = ListNode(value)
            self.tail = self.head
            return
        # Add new head
        self.head.insert_before(value)
        self.head = self.head.prev

    def add_to_tail(self, value):
        # Handle first insertion (setup head and tail)
        if(self.head is None):
            self.add_to_head(value)
            return
        # Add new tail
        self.tail.insert_after(value)
        self.tail = self.tail.next

    def remove_from_head(self):
        head_value = self.head.value
        old_head = self.head
        self.head = self.head.next
        old_head.delete()
        return head_value

    def remove_from_tail(self):
        tail_value = self.tail.value
        old_tail = self.tail
        self.tail = self.tail.prev
        old_tail.delete()
        return tail_value

    def move_to_front(self, node):
        # Remove node from list while maintaining structure
        self.delete(node)
        # Attach current head to new head
        if(self.head):
            node.next = self.head
            self.head.prev = node
        # Set node as new head of list
        node.prev = None
        self.head = node

    def move_to_end(self, node):
        # Remove node from list while maintaining structure
        self.delete(node)
        # Attach current tail to new tail
        if(self.tail):
            node.prev = self.tail
            self.head.prev = node
        # Set node as new tail of list
        node.next = None
        self.tail = node

    def delete(self, node):
        # Remove node and stitch up the resulting gap
        node.delete()
        # Account for removal of node from head or tail
        if(node is self.head):
            self.head = node.next
        if(node is self.tail):
            self.tail = node.next

    def get_max(self):
        max_value = 0
        for value in self:
            if(value > max_value):
                max_value = value
        return max_value

    # - Implement Iterator Interface -------------
    # Just to keep things interesting.
    def __iter__(self):
        return self.IterationHelper(self.head)

    class IterationHelper:
        def __init__(self, start_node):
            self.current_node = start_node

        def __next__(self):
            if(self.current_node is None):
                raise StopIteration
            result = self.current_node.value
            self.current_node = self.current_node.next
            return result

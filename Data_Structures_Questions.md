Answer the following questions for each of the data structures you implemented as part of this project.


## Queue

1. What is the runtime complexity of `enqueue`?
2. What is the runtime complexity of `dequeue`?
3. What is the runtime complexity of `len`?

All three methods run in constant time. There are no loops, recursion, or other
lookups through complex structures. Each method looks directly to a single
stored value.


## Binary Search Tree

1. What is the runtime complexity of `insert`? 
2. What is the runtime complexity of `contains`?
3. What is the runtime complexity of `get_max`?

All three methods run in logarithmic time. Each method must call itself
recursively in order to traverse a tree structure. The number of items at a
specific search depth is the square of that depth.


## Heap

1. What is the runtime complexity of `_bubble_up`?
2. What is the runtime complexity of `_sift_down`?

Both methods run in logarithmic time, as they must recurse through a binary
tree.

3. What is the runtime complexity of `insert`?
4. What is the runtime complexity of `delete`?

Both methods run in logarithmic time, as they depend on the methods _bubble_up
and _sift_down.

5. What is the runtime complexity of `get_max`?

Get max runs in constant time, as it simply returns the first item of an array.


## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
2. What is the runtime complexity of `ListNode.insert_before`?
3. What is the runtime complexity of `ListNode.delete`?

All three methods run in constant time, as they have a set number of
instructions they must perform, with no loops or recursion.

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

All four methods run in constant time, as they have a set number of
instructions they must perform, and the other functions they depend on also run
in constant time.

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
10. What is the runtime complexity of `DoublyLinkedList.delete`?

Likewise, these three methods also run in constant time. The nodes they must
opperate on are stored as variables on the parent object, and can be accessed
directly.

1. a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

The linked list's delete method acts on three nodes at most: The node to be
deleted, and the nodes immediately preceding and following it. This differs
from removing items from a JS array, as JS arrays are implemented as contiguous
blocks of memory. Removing or inserting an item from a JS array there requires
the shifting of all values following that item to new array indices. This
operation requires one set of instructions per moved item, and thus runs in
linear time.

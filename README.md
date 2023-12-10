# Linked List Merger

## Overview

This Python script provides a concise implementation of merging two sorted linked lists. It defines a `ListNode` class for representing nodes in a linked list and a function, `merge_sorted_lists`, for merging two sorted linked lists while adhering to certain constraints.

## `ListNode` Class

### Constructor

- `__init__(self, value=0, next=None)`: Initializes a node with a given value and a reference to the next node. Default values are set to 0 for the value and `None` for the next node.

## `merge_sorted_lists` Function

### Parameters

- `list1`: The first sorted linked list.
- `list2`: The second sorted linked list.

### Returns

- A new linked list representing the merged result of `list1` and `list2`.

### Algorithm Details

1. A dummy node is created as a placeholder for the merged list.
2. A pointer, `current`, is initialized to the dummy node to track the current position in the merged list.
3. A counter, `count`, limits the number of iterations to 50 to control the size of the merged list.
4. The function iterates through both lists, comparing values and merging nodes into the result.
5. A `ValueError` is raised if a node value falls outside the specified range [-100, 100].
6. The merged list is returned, containing at most 50 nodes.

## Example Usage

```python
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = merge_sorted_lists(list1, list2)

while merged_list:
    print(merged_list.value, end=" ")
    merged_list = merged_list.next
```

This example demonstrates merging two sorted linked lists and printing the values of the resulting merged list.

## Constraints

1. The merged list should contain at most 50 nodes.
2. The values of the nodes in both input lists should be within the range [-100, 100].

## Notes

Feel free to adapt and integrate this code into your projects, considering the provided guidelines and constraints. The concise nature of the implementation makes it easy to understand and incorporate into various scenarios where merging sorted linked lists is required.

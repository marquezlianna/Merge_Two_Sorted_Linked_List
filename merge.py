# Define a class for a linked list node
class ListNode:
    # Constructor for the ListNode class with default values
    def __init__(self, value=0, next=None):
        # Initialize the node with a value and a reference to the next node
        self.value = value
        self.next = next

# Define a function to merge two sorted linked lists
def merge_sorted_lists(list1, list2):
    # Create a dummy node as a placeholder for the merged list
    dummy = ListNode()
    # Initialize a pointer to the current node in the merged list
    current = dummy
    # Counter to limit the number of iterations to 50
    count = 0
    
    # Loop while both lists are not empty and the count is less than 50
    while list1 and list2 and count < 50:
        # Check if values are within the specified range [-100, 100]
        if -100 <= list1.value <= 100 and -100 <= list2.value <= 100:
            if list1.value < list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move the current pointer to the last appended node    
            current = current.next
            # Increment the count
            count += 1
        else:
            # Raise an error if node value is outside the specified range
            raise ValueError("Node value outside the range [-100, 100]")
        
    # Append the remaining nodes
    current.next = list1 or list2  

    # Return the next node of the dummy node, which is the merged list
    return dummy.next

# Example usage
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merge the two lists and store the result in merged_list
merged_list = merge_sorted_lists(list1, list2)

# Iterate through the merged list and print each value
while merged_list:
    print(merged_list.value, end=" ")
    merged_list = merged_list.next
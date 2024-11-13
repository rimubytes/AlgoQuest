class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists and returns the merged list

    Parameters:
    list1 (ListNode): The first sorted linked list
    list2 (ListNode): The second sorted linked list

    Returns:
    ListNode: The merged sorted linked list
    """

    # Create a dummy node to serve as the head of the merged list
    dummy = ListNode()
    curr = dummy

    # Traverse both lists and append the smaller value to the merged list
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    # Append the remaining nodes from the non-empty list
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2
    
    # Return the merged list (excluding the dummy node)
    return dummy.next

"""
The `merge_two_lists` function takes two sorted linked lists (`list1` and `list2`) as input and returns a new sorted linked list that is the merge of the two input lists.

Here's how the algorithm works:

1. Create a dummy `ListNode` to serve as the head of the merged list. This helps simplify the logic, as we can start appending nodes to the dummy node's `next` pointer.
2. Initialize a `curr` pointer to the dummy node, which will be used to traverse and build the merged list.
3. Iterate through both `list1` and `list2` while they are not empty:
   - Compare the values of the current nodes in `list1` and `list2`.
   - Append the node with the smaller value to the `curr` node's `next` pointer.
   - Move the corresponding list's pointer to the next node.
   - Move the `curr` pointer to the next node.
4. After the loop, if either `list1` or `list2` is not empty, append the remaining nodes to the end of the merged list.
5. Return the `next` pointer of the dummy node, which is the head of the merged list.
"""
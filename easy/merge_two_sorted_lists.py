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
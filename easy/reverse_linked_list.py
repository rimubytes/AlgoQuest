class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize a ListNode with a value and optional next pointer

        Parameters:
        val (int): The value to be stored in the node
        next (ListNode): Reference to the next node (default is None)
        """
        self.val = val
        self.next = next

def reverse_list_iterative(head: ListNode) -> ListNode:
    """
    Reverses a linked list iteratively

    Parameters:
    head (ListNode): The head of the linked list to be reversed

    Returns:
    ListNode: The head of the reversed linked list

    Time Complexity: 0(n) where n is the number of nodes
    Space Complexity: 0(1) as we only use a constant amount of extra space
    """

    # Initialize previous pointer as None
    prev = None
    # Start with the current pointer at head
    current = head

    # Traverse through the linked list
    while current is not None:
        # Store the next pointer before we change it
        next_temp = current.next
        # Reverse the link by pointing current node to previous node
        current.next = prev
        # Move prev pointer to current node
        prev = current
        # Move current pointer to next node
        current = next_temp

    # Return the new head of the reversed list
    return prev

def reverse_list_recursive(head: ListNode) -> ListNode:
    """
    Reverses a linked list recursively

    Parameters:
    head (ListNode): The head of the linked list to be reversed

    Returns:
    ListNode: The head of the reversed linked list

    Time Complexity: 0(n) where n is the number of nodes
    Space Complexity: 0(n) due to the recursive call stack
    """
    # Base case: if head is None or we've reached the last node
    if head is None or head.next is None:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_list_recursive(head.next)

    # Reverse the links
    head.next.next = head
    head.next = None

    return new_head

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    """
    Creates a linked list from a list of values

    Parameters:
    values (List): List of values to create nodes from

    Returns:
    ListNode: Head of the created linked list
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Statement#
# Given the head of a linked list, your task is to check whether the linked list is a palindrome or not.
# Return TRUE if the linked list is a palindrome; otherwise, return FALSE.

# Template for linked list node class

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result
# Template to reverse the linked list

def reverse_linked_list(slow_ptr):
    prev = None
    next = None
    curr = slow_ptr
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# Template for printing the linked list with forward arrows

def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value

        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")


def palindrome(head):
    # Initialize slow and fast pointers to the head of the linked list
    slow = head
    fast = head

    # Find the middle of the linked list using the slow and fast pointers
    while fast and fast.next:
        # move slow one step forward
        slow = slow.next
        # move fast two steps forward
        fast = fast.next.next

    # Reverse the second half of the linked list starting from the middle node
    revert_data = reverse_linked_list(slow)

    # Compare the first half of the linked list with the reversed second half of the linked list
    check = compare_two_halves(head, revert_data)

    # Re-reverse the second half of the linked list to restore the original linked list
    reverse_linked_list(revert_data)

    # Return True if the linked list is a palindrome, else False
    if check:
        return True
    return False


def compare_two_halves(first_half, second_half):
    # Compare the corresponding nodes of the first and second halves of the linked list
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        else:
            first_half = first_half.next
            second_half = second_half.next
    return True

# Driver code
def main():
    input = (
        [2, 4, 6, 4, 2],
        [0, 3, 5, 5, 0],
        [9, 7, 4, 4, 7, 9],
        [5, 4, 7, 9, 4, 5],
        [5, 9, 8, 3, 8, 9, 5],
    )
    j = 1

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(j, ".\tLinked List:", end=" ", sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        head = input_linked_list.head
        print("\n\tIs it a palindrome?", "Yes" if palindrome(head) else "No")
        j += 1
        print("-"*100, "\n")


if __name__ == "__main__":
    main()

# CREATE LINKED LIST FIRST
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        count = 1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count + 1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count += 1
                current = current.next
            # break
        pass

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
linked_list = LinkedList(node1)
linked_list.append(node2)
linked_list.append(node3)
linked_list.append(node4)
linked_list.append(node5)
linked_list.append(node6)
linked_list.append(node7)
linked_list.print()


########################################################################################################################

# Given a singly linked list, remove the nth node from the end of the list and return its head.

# Linked list: 32 → 78 → 65 → 90 → 12 → 44 → NULL
# n = 3
# Output = 32 → 78 → 65 → 12 → 44 → NULL

def remove_nth_last_node(head, n):
    # Point two pointers, right and left, at head.
    right = head
    left = head

    # Move right pointer n elements away from the left pointer.
    for i in range(n):
        right = right.next

    # Removal of the head node.
    if not right:
        return head.next

    # Move both pointers until right pointer reaches the last node.
    while right.next:
        right = right.next
        left = left.next

        # At this point, left pointer points to (n-1)th element.
        # So link it to next to next element of left.
    left.next = left.next.next

    return head


print(remove_nth_last_node(linked_list.head, 3))

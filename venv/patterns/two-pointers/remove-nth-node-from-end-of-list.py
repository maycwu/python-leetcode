# Given a singly linked list, remove the nth node from the end of the list and return its head.

# Linked list: 32 → 78 → 65 → 90 → 12 → 44 → NULL
# n = 3
# Output = 32 → 78 → 65 → 12 → 44 → NULL

class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    def __str__(self):
        result = ''
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


def remove_nth_last_node(head, n):
    return


head = LinkedListNode(23, None)
node1 = LinkedListNode(28, None)
node2 = LinkedListNode(10, None)
node3 = LinkedListNode(5, None)
node4 = LinkedListNode(67, None)
node5 = LinkedListNode(39, None)
node6 = LinkedListNode(70, None)
node7 = LinkedListNode(28, None)

linked_list = LinkedList()
linked_list.insert(head)
linked_list.insert(node1)
linked_list.insert(node2)
linked_list.insert(node3)
linked_list.insert(node4)
linked_list.insert(node5)
linked_list.insert(node6)
linked_list.insert(node7)

print(linked_list)

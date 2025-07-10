class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)


# -----------------------------------------------------------------------------------------------------

# Recursive solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


# Test Case 1: 1 -> 2 -> 3 -> 4 -> 5
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Test Case 1:")
print("Original List:")
print(node1)

sol = Solution()
reversed_list = sol.reverseList(node1)

print("Reversed List:")
print(reversed_list)

# Test Case 2: Single node
single = ListNode(99)
print("\nTest Case 2:")
print("Original List:")
print(single)

reversed_single = sol.reverseList(single)
print("Reversed List:")
print(reversed_single)

# Test Case 3: Empty list
empty = None
print("\nTest Case 3:")
print("Original List:")
print(empty)

reversed_empty = sol.reverseList(empty)
print("Reversed List:")
print(reversed_empty)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = self
        self.next = next

# naive approach with set()
# time - O(n)
# space - O(n)
def has_cycle_naive(head):
    visited = set()
    node = head

    while node is not None:
        if node in visited:
            return True
        visited.add(node)
        node = node.next
    return False

# But we don’t actually need to remember all visited nodes.
# Instead, we can use two pointers moving at different speeds.
# If there’s a cycle, the fast pointer will eventually meet the slow pointer.
# If not, the fast pointer will reach the end of the list.


# Using Floyd’s Tortoise & Hare algorithm (fast/slow pointers)
# time - O(n)
# space - O(1)
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next #shift by 2

        # checks if these two pointers point to the exact same node in memory
        if slow == fast:
            return True

    return False



# Create a list 1 -> 2 -> 3 -> 4 and then link 4 -> 2 (cycle)
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = b  # creates cycle

print(has_cycle_naive(a)) # True
print(has_cycle(a)) # True

# No-cycle example
x = ListNode(10)
y = ListNode(20)
x.next = y
print(has_cycle_naive(x))  # False
print(has_cycle(x)) # False

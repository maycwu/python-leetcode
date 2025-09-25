from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursion
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1 is None:
#             return list2
#
#         if list2 is None:
#             return list1
#
#         if list1.val <= list2.val:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         else:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy

        # List 1: 1->2->5
        # List 2: 1->3->4

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next


def print_list(node: Optional[ListNode]) -> str:
    """Helper function to convert linked list to string for display."""
    result = []
    current = node
    while current:
        result.append(str(current.val))
        current = current.next
    return "->".join(result) if result else "Empty List"

# Test cases
if __name__ == "__main__":
    # Test case 1: Both lists are non-empty
    # List 1: 1->2->5
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    # List 2: 1->3->4
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    solution = Solution()
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 1: {print_list(merged)}")  # Expected: 1->1->2->3->4->4
    
    # Test case 2: First list is empty
    list1 = None
    list2 = ListNode(0)
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 2: {print_list(merged)}")  # Expected: 0->None
    
    # Test case 3: Second list is empty
    list1 = ListNode(1)
    list2 = None
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 3: {print_list(merged)}")  # Expected: 1->None
    
    # Test case 4: Both lists are empty
    list1 = None
    list2 = None
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 4: {print_list(merged)}")  # Expected: Empty List

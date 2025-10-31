# TODO: Implement this function
"""
206. Reverse Linked List (Easy)

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000
"""

from linked_list_utils import ListNode, list_to_linkedlist, linkedlist_to_list

def reverseList(head: ListNode) -> ListNode:
    pass

# Test cases
test_cases = [
    ([1,2,3,4,5], [5,4,3,2,1]),
    ([1,2], [2,1]),
    ([], []),
    ([1], [1]),
    ([1,2,3], [3,2,1])
]

for input_list, expected in test_cases:
    head = list_to_linkedlist(input_list)
    result = reverseList(head)
    result_list = linkedlist_to_list(result)
    print(f"Input: {input_list}")
    print(f"Output: {result_list}")
    print(f"Expected: {expected}")
    print("✅" if result_list == expected else "❌")
    print()
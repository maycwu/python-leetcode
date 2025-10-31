# TODO: Implement this function
"""
234. Palindrome Linked List (Easy)

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9
"""

from linked_list_utils import ListNode, list_to_linkedlist

def isPalindrome(head: ListNode) -> bool:
    pass

# Test cases
test_cases = [
    ([1,2,2,1], True),
    ([1,2], False),
    ([1], True),
    ([1,2,3,2,1], True),
    ([1,2,3,4], False),
    ([1,0,1], True)
]

for lst, expected in test_cases:
    head = list_to_linkedlist(lst)
    result = isPalindrome(head)
    print(f"Input: {lst}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print("✅" if result == expected else "❌")
    print()
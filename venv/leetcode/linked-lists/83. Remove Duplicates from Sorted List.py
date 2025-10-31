# TODO: Implement this function

"""
83. Remove Duplicates from Sorted List (Easy)

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.
"""

from linked_list_utils import ListNode, list_to_linkedlist, linkedlist_to_list

def deleteDuplicates(head: ListNode) -> ListNode:
    pass

# Test cases
test_cases = [
    ([1,1,2], [1,2]),
    ([1,1,2,3,3], [1,2,3]),
    ([], []),
    ([1,1,1], [1]),
    ([1,2,3,4,5], [1,2,3,4,5])
]

for input_list, expected in test_cases:
    head = list_to_linkedlist(input_list)
    result = deleteDuplicates(head)
    result_list = linkedlist_to_list(result)
    print(f"Input: {input_list}")
    print(f"Output: {result_list}")
    print(f"Expected: {expected}")
    print("✅" if result_list == expected else "❌")
    print()
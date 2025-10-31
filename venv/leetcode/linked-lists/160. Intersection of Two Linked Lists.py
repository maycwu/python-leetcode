# TODO: Implement this function

"""
160. Intersection of Two Linked Lists (Easy)

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal is 0, while skipA and skipB cannot be used and are set to 0.

Constraints:
- The number of nodes of listA is in the m.
- The number of nodes of listB is in the n.
- 1 <= m, n <= 3 * 10^4
- 1 <= Node.val <= 10^5
- 0 <= skipA < m
- 0 <= skipB < n
- intersectVal is 0 if listA and listB do not intersect.
- intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
"""

from linked_list_utils import ListNode, list_to_linkedlist

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    pass

# Helper function to create intersection
def create_intersection(listA, listB, skipA, skipB):
    if skipA < 0 or skipB < 0:
        return list_to_linkedlist(listA), list_to_linkedlist(listB)

    # Create list A
    dummyA = ListNode(0)
    currentA = dummyA
    intersect_node = None
    for i in range(len(listA)):
        node = ListNode(listA[i])
        if i == skipA:
            intersect_node = node
        currentA.next = node
        currentA = currentA.next

    # Create list B
    dummyB = ListNode(0)
    currentB = dummyB
    for i in range(skipB):
        node = ListNode(listB[i])
        currentB.next = node
        currentB = currentB.next

    # Link to intersection
    if intersect_node:
        currentB.next = intersect_node

    return dummyA.next, dummyB.next

# Test cases
test_cases = [
    ([4,1,8,4,5], [5,6,1,8,4,5], 2, 3, 8),  # Intersect at 8
    ([1,9,1,2,4], [3,2,4], 3, 1, 2),       # Intersect at 2
    ([2,6,4], [1,5], 3, 2, None),          # No intersection
    ([1], [1], 0, 0, 1),                   # Single node intersection
    ([2,4,6], [1,3], 2, 2, None)           # No intersection
]

for listA, listB, skipA, skipB, expected_val in test_cases:
    headA, headB = create_intersection(listA, listB, skipA, skipB)
    result = getIntersectionNode(headA, headB)
    result_val = result.val if result else None
    print(f"listA = {listA}, listB = {listB}")
    print(f"Expected intersection value: {expected_val}")
    print(f"Found intersection value: {result_val}")
    print("✅" if result_val == expected_val else "❌")
    print()
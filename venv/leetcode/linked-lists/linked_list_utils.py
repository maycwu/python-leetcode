"""
Definition for singly-linked list.
This file should be imported in other linked list problem solutions.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(lst):
    """Helper function to convert a list to a linked list"""
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    """Helper function to convert a linked list to a list"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
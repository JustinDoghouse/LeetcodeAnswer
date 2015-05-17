__author__ = 'burger'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        h = ptr = ListNode(0)
        ptr.next = head
        while ptr.next and ptr.next.next:
            tmp = ptr.next
            ptr.next = tmp.next
            tmp.next = ptr.next.next
            ptr.next.next = tmp
            ptr = tmp
        return h.next
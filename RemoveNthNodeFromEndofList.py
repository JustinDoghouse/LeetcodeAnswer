__author__ = 'burger'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        torm, totail = head, head
        i = 0
        while i < n:
            i += 1
            totail = totail.next
        if totail == None:
            return head.next
        while totail.next != None:
            totail = totail.next
            torm = torm.next
        torm.next = torm.next.next
        return head

__author__ = 'burger'
# CAN'T FIX THE PROBLEM
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head:
            return head
        return mergesort(head)


def mergesort(first):
    if not first or not first.next:
        return first
    mid = getmid(first)
    second = mid.next
    mid.next = None
    second = mergesort(second)
    first = mergesort(first)
    return mergetwo(first, second)


def getmid(first):
    slow = first
    fast = first
    while slow and fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def mergetwo(l1, l2):
    head = ListNode(0)
    ptr = head
    while l1 and l2:
        if l1.val > l2.val:
            ptr.next = l1
            l1 = l1.next
        else:
            ptr.next = l2
            l2 = l2.next
    if l1:
        ptr.next = l1
    else:
        ptr.next = l2
    return head.next
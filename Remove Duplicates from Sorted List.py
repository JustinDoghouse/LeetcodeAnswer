__author__ = 'burger'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        this = head
        while this and this.next:
            if this.next:
                if this.next.val == this.val:
                    this.next = this.next.next
                else:
                    this = this.next

        return head

__author__ = 'burger'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def connect(sml, lrg):
    if not sml.next:
        sml.next = lrg
        return sml, None
    stmp = lrg
    while lrg.next and lrg.next.val < sml.next.val:
        lrg = lrg.next
    ltmp = lrg
    ltmp.next = sml.next
    sml.next = stmp
    return ltmp.next, lrg.next


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        tmp = head = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        else:
            tmp.next = l2
        return head.next


    def mergeTwoLists_TLE(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1

        if l1.val < l2.val:
            head = l1
            l1, l2 = connect(l1, l2)
        else:
            head = l2
            l1, l2 = connect(l2, l1)
        while l1 and l2:
            if not l1.next:
                l1.next = l2
                break
            if l2.val < l1.next.val:
                l1, l2 = connect(l1, l2)
            else:
                l1 = l1.next
        return head


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(3)
    l2 = ListNode(1)
    print(s.mergeTwoLists(l1, l2).val)

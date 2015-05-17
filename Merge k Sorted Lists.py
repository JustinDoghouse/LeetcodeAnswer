__author__ = 'burger'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):  # 477
        if not lists:
            return None
        lgh = len(lists)
        if lgh == 1:
            return lists[0]
        if lgh == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        return self.mergeTwoLists(self.mergeKLists(lists[:lgh // 2]), self.mergeKLists(lists[lgh // 2:]))

    def mergeKLists_some_stupid_way(self, lists):  # 580 ms
        t = self.mergeKLists1(lists)
        if not t:
            return None
        return t

    def mergeKLists1(self, lists):
        if not lists:
            return None
        lst = [x for x in lists if x]
        lgh = len(lst)
        if lgh == 1:
            return lst
        tmp = []
        if lgh % 2:
            tmp.append(lst[lgh - 1])
        for i in range(0, lgh // 2):
            tmp.append(self.mergeTwoLists(lst[2 * i], lst[2 * i + 1]))
        return self.mergeKLists1(tmp)

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

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        for i in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        node_to_delete = second.next
        second.next = node_to_delete.next

        return dummy.next

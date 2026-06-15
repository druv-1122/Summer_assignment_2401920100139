class Solution(object):
    def middleNode(self, head):
        if head is None:
            return None

        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None:
            if fast_pointer.next is None:
                break

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer

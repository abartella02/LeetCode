from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Map method O(n), O(n)"""
        seen = []
        master_head = head
        while head is not None:
            seen.append(head)
            head = head.next

        if len(seen) == 1 and n == 1:
            master_head = None
            return master_head

        pos = len(seen) - n
        node = seen[pos]
        if pos > 0 and pos < len(seen) - 1:
            seen[pos - 1].next = seen[pos + 1]
        elif pos == 0:
            master_head = seen[1]
        elif pos == len(seen) - 1:
            seen[pos - 1].next = None

        node.next = None

        return master_head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """fast and slow method O(n), O(1)"""
        fast = head
        slow = head

        for _ in range(n):
            # increment n nodes
            # if fast is null before/when n is reached, need to remove first pointer
            # i.e. 1 -> 2 -> 3, n = 3
            #      on third advance, n will be null, therefore 1 is the node to remove
            fast = fast.next
            if fast is None:
                head = slow.next
                slow.next = None
                return head

        # advance fast and slow to find the node at position n
        # the gap between fast and slow is of length n, so when
        # fast reaches the end, slow will be at len(list) - n
        # we want slow to be at len(list) - n - 1, so that we can properly manipulate
        # so, we want fast to stop at the second last element, where fast.next = None
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next  # remove the node at n

        return head

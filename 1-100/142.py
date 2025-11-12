from typing import *


# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # catch short list case
        if fast is None or fast.next is None or fast.next.next is None:
            return None

        while fast is not None and fast.next is not None:  # catch non cycle
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # there is a cycle
                break
        else:
            return None  # run if the loop exits naturally (not break)

        slow = head  # reset slow
        while slow != fast:
            slow = slow.next  # they meet again at the start of the cycle
            fast = fast.next
        return slow  # return start of cycle

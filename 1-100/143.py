"""
Reorder list
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

"""

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list(x, y):
    head = ListNode(x, None)
    prev = head
    for i in range(2, y + 1):
        prev.next = ListNode(i, None)
        prev = prev.next
    return head


class Solution:
    def reorderListBruteForce(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # brute force
        def goToSecondLast(head):
            while head.next.next is not None:
                head = head.next
            return head

        masterhead = head
        while head.next is not None and head.next.next is not None:
            start = head  # first node
            new_end = goToSecondLast(head)  # second last node
            insert = new_end.next  # last node
            follow = start.next  # second node

            start.next = insert  # first node points to old last node
            insert.next = follow  # old last node points to old 2nd node
            new_end.next = None  # new last node points to null

            temp = []
            temphead = masterhead
            while temphead is not None:
                temp.append(temphead.val)
                temphead = temphead.next
            print(temp)

            head = head.next.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def findMiddle(head):
            slow, fast = head, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            return slow

        def reverse(head):
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        def merge(head1, head2):
            """Merge two singly linked lists of equal length"""
            master_head = head1
            while head1 and head2:
                temp = head1.next
                temp2 = head2
                head2 = head2.next

                head1.next = temp2
                temp2.next = temp
                head1 = temp
            return master_head

        # code start

        mid = findMiddle(head)
        head1 = head
        head2 = mid.next
        mid.next = None  # disconnect the lists

        head2 = reverse(head2)

        merge(head1, head2)


s = Solution()
head = make_list(1, 5)
s.reorderList(head)

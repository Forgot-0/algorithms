# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = head
        while lst.next:
            lst.val, lst.next.val = lst.next.val, lst.val
            lst = lst.next
            if lst == None:
                break
        return head
    
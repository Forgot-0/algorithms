from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll = ans = head
        count = 0
        while ll:
            count += 1
            ll = ll.next
        l = count - n
        for i in range(l-1):
            ans = ans.next
        
        if l == 0:
            return head.next
        elif ans.next:
            ans.next = ans.next.next
        else:
            return


        return head
        


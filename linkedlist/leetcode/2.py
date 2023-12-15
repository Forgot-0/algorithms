from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        i = 0
        
        while l1:
            num1 += l1.val*10**i
            i += 1
            l1 = l1.next

        i=0
        while l2:
            num2 += l2.val*10**i
            i += 1
            l2 = l2.next

        res = num1 + num2
        listnode = ans = ListNode(res%10)
        res //= 10
        while res:
            listnode.next = ListNode(res%10)
            res //= 10
            listnode = listnode.next
        return ans
        
s = Solution()

l1 = ListNode()


print(s.addTwoNumbers())


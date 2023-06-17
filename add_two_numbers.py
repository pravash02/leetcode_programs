# https://leetcode.com/problems/add-two-numbers/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""

        while l1:
            s1 += str(l1.val)
            l1 = l1.next

        while l2:
            s2 += str(l2.val)
            l2 = l2.next

        s = str(int(s1) + int(s2))[::-1]

        head = ListNode(int(s[0]))
        current = head

        for digit in s[1:]:
            current.next = ListNode(int(digit))
            current = current.next

        return head


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2:
            sum_val = carry

            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next

            carry = sum_val // 10   # 10|7|0, 10|10|1
            curr.next = ListNode(sum_val % 10)
            curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    head_l1 = ListNode(l1[0])
    current = head_l1
    for digit in l1[1:]:
        current.next = ListNode(int(digit))
        current = current.next

    head_l2 = ListNode(l2[0])
    current = head_l2
    for digit in l2[1:]:
        current.next = ListNode(int(digit))
        current = current.next

    print(sol.addTwoNumbers(l1=head_l1, l2=head_l2))
    print(sol2.addTwoNumbers(l1=head_l1, l2=head_l2))

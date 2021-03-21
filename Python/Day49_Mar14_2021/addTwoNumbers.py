# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        res_ptr =result
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            add = x+y+carry
            carry = add//10
            node = ListNode(add%10)
            res_ptr.next = node
            res_ptr = res_ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            res_ptr.next = ListNode(carry)
        
        return result.next
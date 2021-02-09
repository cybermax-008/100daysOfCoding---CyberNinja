# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        carry = 0
        curr_res = result
        p =l1
        q =l2
        while p or q:
            x,y=0,0
            if p is not None:
                x = p.val
            if q is not None:
                y = q.val
            add = x+y+carry
            carry = add//10
            curr_res.next = ListNode(add%10)
            curr_res = curr_res.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if carry >0:
            curr_res.next = ListNode(carry)
        
        return result.next
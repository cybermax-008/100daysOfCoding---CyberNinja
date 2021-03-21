# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = head
        prev_node = None
        while curr_node:
            dup = 0
            while curr_node.next and curr_node.val == curr_node.next.val:
                curr_node = curr_node.next
                dup+=1
            if dup:
                if prev_node:
                    prev_node.next = curr_node.next
                    curr_node = curr_node.next
                else:
                    head =curr_node.next
                    curr_node = head
            else:
                prev_node = curr_node
                curr_node = curr_node.next
        return head
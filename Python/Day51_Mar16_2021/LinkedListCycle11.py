# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = {}
        while head:
            if head in visited:
                return visited[head]
            visited[head] = head
            head = head.next
        return 
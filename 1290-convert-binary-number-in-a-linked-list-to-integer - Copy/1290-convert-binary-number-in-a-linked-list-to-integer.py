# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        num=0
        count=0
        length=0
        node=head
        while node:
            length=length+1
            node=node.next
        node=head
        length=length-1
        while node:
            num=num+(pow(2,length)*(node.val))
            length=length-1
            node=node.next
        
        return num



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next == None:
            return None
        
        temp = head
        i = 0
        while (temp!=None):
            i+=1
            temp = temp.next
             
        if i==2:
            head.next = None
            return head
        
        n=i//2
        i = 1
        temp=head
        while(i<n and temp!=None):
            temp = temp.next
            i+=1
        temp.next = temp.next.next
        return head
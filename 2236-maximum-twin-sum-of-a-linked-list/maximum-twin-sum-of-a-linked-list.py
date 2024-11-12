# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        i = 0
        val_list = []
        while temp!=None:
            i+=1
            val_list.append(temp.val)
            temp = temp.next
        
        total_len = i
        n = i//2
        i=0
        temp=head
        print(val_list)
        print(n)
        max_sum = 0
        while(i<n and temp!=None): 
            sum1 = temp.val + val_list[total_len-1-i]
            print("SUM1: ", sum1)
            max_sum = max(sum1,max_sum)
            temp = temp.next
            i+=1
        return max_sum

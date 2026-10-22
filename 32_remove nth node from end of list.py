# Given the head of a linked list, remove the nth node from the end of the list and return its head
# LOGIC:
# 1.pahle ptr1 ko head pr rakhenge aur puri list ki length find krenge.
# 2.agar length==n hai to first node delete krne ke liye head.next return kr denge.
# 3.fir n jis node pr hai uske ek node pahle tak jayenge.
# 4.Ab us node ke next me uske next.next(ptr1.next=ptr1.next.next)dal denge.
# 5.uske baad head ko return kr denge.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """                                               # PSEUDO CODE:
                                                       # START
        ptr1=head                                      # 1.set ptr1=head
        length=0                                       # 2.length=0
        while ptr1 is not None:                        # 3.Repeat step 4&5 while ptr1 is not none
            ptr1=ptr1.next                             # 4.set ptr1=ptr1.next 
            length+=1                                  # 5.length+=1
        if n==length:                                  # 6.if n==length
            return head.next                           # 7. return head.next
        ptr1=head                                      # again step 1     
        i=1                                            # 8.set i=1   
        while(i<length-n):                             # 9.Repeat step 10&11 while(i<length-n)
            ptr1=ptr1.next                             # 10.set ptr1=ptr1.next 
            i+=1                                       # 11.set i+=1
        ptr1.next=ptr1.next.next                       # 12.set ptr1.next=ptr1.next.next 
        return head                                    # 13.return head
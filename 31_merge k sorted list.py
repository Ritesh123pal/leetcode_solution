# Merge all the linked-lists into one sorted linked-list and return it.
# LOGIC:
# 1. pahle ek empty list banaye jisme hum sabhi linked list ke elements ko store karenge.
# 2. Ek loop chalao jisme hum sabhi linked list ke elements ko ans me append karenge.
# 3. ans ko sort kar do.
# 4. Ek new linked list banaye jisme hum sorted elements ko store karenge.
# 5. Ek loop chalao jisme hum ans ke elements ko new linked list me append karenge.
# 6. new linked list ke head.next ko return karo.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """                                       # PSEUDO CODE:                   
                                              # START
        ans=[]                                # 1.set ans=[] (empty list)
        for x in lists:                       # 2.loop through each linked list in lists: 
            while x:                          # 3.loop through each node in the linked list:  
                ans.append(x.val)             # 4.append x.val to ans  
                x=x.next                      # 5.move to the next node in the linked list
        ans.sort()                            # 6.sort ans   
        head=ListNode(0)                      # 7.set head=ListNode(0) (dummy node)
        current=head                          # 8.set current=head (YE DUMMY NODE KO POINT KAR RAHA HAI)
        for val in ans:                       # 9.loop through each value in ans:  
            current.next=ListNode(val)        # 10.set current.next=ListNode(val) (VAL KA USE KRKE NAYA NODE BANAYENGE AUR USKO CURRENT KE NEXT ME POINT KARENGE)  
            current=current.next              # 11.AB AGLE NODE KO CURRENT ME SET KARDO (current=current.next)
        return head.next                      # 12.return head.next (YE DUMMY NODE KE NEXT KO RETURN KAREGA, JO KI ACTUAL MERGED LINKED LIST KA HEAD HAI)  
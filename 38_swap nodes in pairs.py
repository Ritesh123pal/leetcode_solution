# Given a linked list, swap every two adjacent nodes and return its head.
# LOGIC:
# 1.sabse pahle head ko check krenge ki wo None to nhi hai ya fir uska next None to nhi hai.
# 2. agar condition false hai to head ko return kr denge.
# 3. agar condition true hai to ek dummy node create karenge jo head ke pehle point karega.
# 4. ek prev pointer create krenge jo dummy node ko point karega.
# 5. ab while loop chalayenge jab tak prev ka next aur prev ka next ka next None nhi hai.
# 6. loop ke andar prev ka next ko ptr me store krenge aur ptr ka next ko ptr1 me store krenge.
# 7. ab ptr ka next ko ptr1 ka next se point krenge aur ptr1 ka next ko ptr se point krenge.
# 8. ab prev ka next ko ptr1 se point krenge aur prev ko ptr se point krenge.
# 9.ab ptr aur ptr1 ko update krenge aur loop continue krenge.
# 10. loop ke baad dummy ka next return krenge jo new head hoga.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """                                                 # PSEUDO CODE:
                                                          #START:
        ptr=head                                          # 1. ptr=head
        if ptr is None or ptr.next is None:               # 2. if ptr is None or ptr.next is None:
            return head                                   # 3. return head 
        dummy=ListNode(0)                                 # 4. create a dummy node with value 0
        dummy.next=head                                   # 5. dummy.next=head
        prev=dummy                                        # 6. prev=dummy
        while prev.next and prev.next.next is not None:   # 7. repeat steps.....while prev.next and prev.next.next is not None:   
            ptr=prev.next                                           # 8. ptr=prev.next
            ptr1=ptr.next                                           # 9. ptr1=ptr.next 
            ptr.next=ptr1.next                                      # 10. ptr.next=ptr1.next 
            ptr1.next=ptr                                           # 11. ptr1.next=ptr
            prev.next=ptr1                                          # 12. prev.next=ptr1
            prev=ptr                                                # 13. prev=ptr     
        return dummy.next                                 # 14. return dummy.next  
                                                          # END:
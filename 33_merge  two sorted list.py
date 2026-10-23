# You are given the heads of two sorted linked lists list1 and list2
# LOGIC:
# 1.Agar list1 empty hai, toh list2 ko use karo.
# 2.Warna list1 ke last node tak jaakar list2 ko jod do.
# 3.Dono lists ki values ko ans mein store karo.
# 4.ans.sort() se values sort karo.
# 5.Sorted values se nayi linked list banao.
# 6..next return karo, kyunki head dummy node hai.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """                                                # PSEUDO CODE:
                                                       # START
        if list1 is None:                             # 1.IF LIST1 IS NULL:
            list1=list2                                   # LIST1=LIST2
        else:                                          # 2.ELSE: 
            ptr=list1                                    # PTR=LIST1
            while ptr.next is not None :                 # WHILE PTR.NEXT !=NULL
                ptr=ptr.next                                # PTR=PTR.NEXT 
            ptr.next=list2                               # PTR.NEXT=LIST2  
        ans=[]                                         # 3.SET ANS=[]
        ptr=list1                                      # 4.SET PTR=LIST1 
        while ptr is not None:                         # 5.WHILE PTR!=NULL   
            ans.append(ptr.val)                           # ANS.APPEND(PTR.VAL)
            ptr=ptr.next                                  # SET PTR=PTR.NEXT
        ans.sort()                                     # 6.ANS.SORT() 
        head=ListNode(0)                               # 7.SET HEAD=LISTNODE(0) 
        current=head                                   # 8.SET CURR=HEAD 
        for val in ans:                                # 9. FOR VAL IN ANS
            current.next=ListNode(val)                    # SET CURR.NEXT=LISTNODE(VAL)
            current=current.next                          # SET CURR=CUR.NEXT
        return head.next                               # 10.RETURN HEAD.NEXT
                                                       # END 
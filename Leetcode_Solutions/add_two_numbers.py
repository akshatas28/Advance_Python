# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current1= l1
        normallist1 = []

        while current1 is not None:
            normallist1.append(current1.val)
            current1= current1.next
        normallist1.reverse()
        current2= l2
        normallist2= []

        while current2 is not None:
            normallist2.append(current2.val)
            current2= current2.next
        normallist2.reverse()
        l3str = "".join(str(i) for i in normallist1)
        l3int=int(l3str)
        l4str = "".join(str(i) for i in normallist2)
        l4int=int(l4str)
        l5int = l3int + l4int
        l5str=str(l5int)
        l5=[int(character) for character in l5str]
        l5.reverse()
        dummy = ListNode(0)
        current = dummy
        for num in l5:
            current.next = ListNode(num) 
            current = current.next
        return dummy.next
        
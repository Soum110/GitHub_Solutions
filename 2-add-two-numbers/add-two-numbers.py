# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        L1 = []
        curr1 = l1
        while curr1 != None:
            L1.append(int(curr1.val))
            curr1 = curr1.next

        L2 = []
        curr2 = l2

        while curr2 != None:
            L2.append(int(curr2.val))
            curr2 = curr2.next

        L1 = int("".join(map(str ,list(L1[::-1])))) if L1 else 0
        L2 = int("".join(map(str ,list(L2[::-1])))) if L2 else 0
        res = L1 + L2
        res = list(map(int, str(res)))

        def createLL(res, n):
            if n <= 0:
                return None
            p = ListNode(val = res[n-1], next = createLL(res, n-1))
            return p

        return createLL(res, len(res))

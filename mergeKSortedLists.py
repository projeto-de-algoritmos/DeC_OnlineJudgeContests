# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, A: ListNode, B: ListNode) -> ListNode:
        if not A: return B
        if not B: return A
        if A.val < B.val:
            aux = self.merge(A.next, B)
            return ListNode(val=A.val, next=aux)
        else:
            aux = self.merge(A, B.next)
            return ListNode(val=B.val, next=aux)
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        middle = len(lists)//2
        if not lists: return
        if len(lists) == 1: return lists[0]
        left = self.mergeKLists(lists[:middle])
        right = self.mergeKLists(lists[middle:])

        result = self.merge(left, right)
        return result
    
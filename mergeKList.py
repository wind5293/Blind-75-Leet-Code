# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def buildLinkedList(values):
    temp = ListNode()
    curr = temp
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
        
    return temp.next

def printLinkedList(head: Optional[ListNode]):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    
    print(values)
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # C1: brute force
        # values = []
        
        # for list in lists:
        #     while list:
        #         values.append(list.val)
        #         list = list.next
        
        # values.sort()
        # return buildLinkedList(values)
    
        # C2: merge pairwise
        def mergeTwoList(l1: Optional[ListNode], l2: Optional[ListNode]):
            dummy = ListNode()
            curr = dummy
            
            while l1 and l2:
                if l1.val == l2.val:
                    curr.next = ListNode(l1.val)
                    curr = curr.next 
                    curr.next = ListNode(l2.val)
                    l1 = l1.next
                    l2 = l2.next
                
                elif l1.val < l2.val:
                    curr.next = ListNode(l1.val)
                    l1 = l1.next
                
                else:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next
                curr = curr.next
            
            curr.next = l1 if l1 else l2
            return dummy.next
        
        while len(lists) > 1:
            merge = []
            # Ý tưởng: nối 2 list liền kề nhau, đưa vào 1 mảng chứa linked list. Sau đó thay thế lists bằng mảng đó
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None     
                merge.append(mergeTwoList(l1, l2))
            lists = merge
        return lists[0] if lists else None
        
        
l1 = buildLinkedList([1, 4, 5])
l2 = buildLinkedList([1, 3, 4])
l3 = buildLinkedList([2, 6])
l4 = buildLinkedList([])
l5 = buildLinkedList([7])
lists = [l1, l2, l3, l4, l5]

solution = Solution()
printLinkedList(solution.mergeKLists(lists))
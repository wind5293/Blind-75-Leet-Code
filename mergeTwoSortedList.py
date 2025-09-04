from typing import Optional

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        curr = temp
        
        while list1 and list2:
            # Kiểm tra điều kiện bằng của 2 node giúp giảm thời gian chạy 
            if list1.val == list2.val:
                curr.next = ListNode(list1.val)
                curr = curr.next
                curr.next = ListNode(list2.val)
                
                list1 = list1.next
                list2 = list2.next
            
            elif list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 if list1 else list2
        return temp.next
        

values1 = [1, 3, 5, 6, 7, 10]
values2 = [1, 2, 4, 5, 8]
list1 = buildLinkedList(values1)
list2 = buildLinkedList(values2)

solution = Solution()
res = printLinkedList(solution.mergeTwoLists(list1, list2))
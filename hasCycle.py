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

def build_cycle_list():
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2   # cycle ở đây (trỏ về node 2)

    return n1

def printLinkedList(head: Optional[ListNode]):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    
    print(values)
    
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Cách 1: lưu từng node đi qua vào trong set, nếu lặp lại trong set thì linked list là cycle
        # list_val = set()
        
        # dummy = head
        # while dummy:
        #     if dummy.val in list_val:
        #         return True
        #     else:
        #         list_val.add(dummy.val)
        #         dummy = dummy.next
        # 
        # return False
        
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
        
    
linked_list = build_cycle_list()
solution = Solution()
print(solution.hasCycle(linked_list))
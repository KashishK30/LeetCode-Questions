# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_cp = -1
        last_cp = -1
        min_dist = float('inf')
        max_dist = float('-inf')
        
        prev = head
        curr = head.next
        i = 1
        
        while curr and curr.next:
            if (curr.val < curr.next.val and prev.val > curr.val) or (curr.val > curr.next.val and prev.val < curr.val):
                if first_cp == -1:
                    first_cp = i
                else:
                    min_dist = min(min_dist, i - last_cp)
                    max_dist = max(max_dist, i - first_cp)
                last_cp = i
            prev = curr
            curr = curr.next
            i += 1
            
        if first_cp == last_cp:
            return [-1, -1]
        else:
            return [min_dist, max_dist]        
        
def helper(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head

    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
        
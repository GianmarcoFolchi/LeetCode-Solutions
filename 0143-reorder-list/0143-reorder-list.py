# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #return if size <= 2
        if not head or not head.next or not head.next.next: 
            return head
        #find middle of linked list 
        slow, runner = head, head
        while runner and runner.next: 
            slow = slow.next
            runner = runner.next.next
        slow.next = reverseList(slow.next)
        rListRunner = slow.next
        runner = head
        slow.next = None

        while rListRunner:
            tmp = rListRunner.next
            insert(runner, rListRunner)
            runner = runner.next.next
            rListRunner = tmp

def insert(head, val): 
    tmp = head.next
    head.next = val
    val.next = tmp 

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head: 
        return head
    l, m, r = None, head, head.next

    while r: 
        m.next = l
        l = m 
        m = r 
        r = r.next
    
    m.next = l
    return m
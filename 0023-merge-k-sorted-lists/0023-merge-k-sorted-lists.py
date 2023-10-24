# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: 
            return None
        mergedList = lists
        while len(lists) != 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1 < len(lists)) else None
                tmpList = mergeTwoLists(l1, l2)
                mergedList.append(tmpList)
            lists = mergedList

        return lists[0]


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1 and not list2) or not list2: 
            return list1
        if not list1:
            return list2
        
        res, l1R, l2R = list1, list1, list2
        if list1.val < list2.val:
            res, l1R, l2R = list1, list1, list2
        else: 
            res, l1R, l2R = list2, list2, list1

        def insert(head, val): 
            tmp = head.next
            head.next = val
            val.next = tmp 
    
        while l1R or l2R: 
            if not l2R or not l1R: 
                return res

            if l1R.val == l2R.val or (l1R.val < l2R.val and not l1R.next) or (l1R.val < l2R.val and l1R.next and l1R.next.val > l2R.val): 
                tmp = l2R
                l2R = l2R.next
                insert(l1R, tmp)
                l1R = l1R.next
            else: 
                l1R = l1R.next
        return res
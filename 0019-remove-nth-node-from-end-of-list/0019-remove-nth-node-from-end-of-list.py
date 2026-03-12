class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = slow = dummy
        
        # move fast pointer n steps
        for _ in range(n):
            fast = fast.next
        
        # move both pointers
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # remove node
        slow.next = slow.next.next
        
        return dummy.next
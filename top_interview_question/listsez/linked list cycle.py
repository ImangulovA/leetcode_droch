class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
# https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/ hare tortoise

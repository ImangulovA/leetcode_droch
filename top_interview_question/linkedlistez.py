# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    # - Initialize two pointers slow and fast pointing to the head of the list.
    #
    # - Loop while n > 0
    #   - fast = fast->next
    #   - decrement n--
    #
    # // if fast is nil it means the first node is supposed to be removed
    # - if fast == nil
    #   - head = head->next
    #   - return head
    #
    # - Loop while fast->next != nil
    #   - slow = slow->next
    #   - fast = fast->next
    #
    # - if slow->next != nil && slow->next->next
    #   - slow->next = slow->next->next
    # - else
    #   - slow->next = nil
    # - end
    #
    # return head
    # from https://medium.com/nerd-for-tech/leetcode-remove-nth-node-from-end-of-list-3e7902c4c2af

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        potwo = head
        while n > 0:
            pointer = pointer.next
            n -= 1
        if pointer == None:
            head = head.next
        else:
            while pointer.next != None:
                pointer = pointer.next
                potwo = potwo.next
            if (potwo.next != None) and (potwo.next.next != None):
                potwo.next = potwo.next.next
            else:
                potwo.next = None
        return head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None

        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next

    # Function to check if two input
    # lists have same data
    def compareLists(self, head1, head2):

        temp1 = head1
        temp2 = head2

        while (temp1 and temp2):
            if (temp1.data == temp2.data):
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return 0

        # Both are empty return 1
        if (temp1 == None and temp2 == None):
            return 1

        # Will reach here when one is NULL
        # and other is not
        return 0

    # Function to check if given
    # linked list is palindrome or not
    def isPalindrome(self, head):
        slow_ptr = head
        
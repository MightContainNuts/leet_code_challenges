#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import Optional, List


l1_test = [2, 4, 3]
l2_test = [5, 6, 4]
answer = [7, 0, 8]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_current, l2_current = l1, l2
        carry = 0
        result_head = None
        result_tail = None
        while l1_current or l2_current or carry:
            val1 = l1_current.val if l1_current else 0
            val2 = l2_current.val if l2_current else 0

            current_sum = val1 + val2 + carry
            carry = current_sum // 10
            current_sum = current_sum % 10

            result_node = ListNode(current_sum)
            if result_head is None:
                result_head = result_node
                result_tail = result_node
            else:
                result_tail.next = result_node
                result_tail = result_node

            print( l1_current.val, l2_current.val, current_sum, carry)
            if l1_current:
                l1_current = l1_current.next
            if l2_current:
                l2_current = l2_current.next

        return result_head


    @staticmethod
    def list_to_linkedlist(lst):
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head



if __name__ == '__main__':
    s = Solution()
    l1 = s.list_to_linkedlist(l1_test)
    l2 = s.list_to_linkedlist(l2_test)
    answer = s.list_to_linkedlist(answer)
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next

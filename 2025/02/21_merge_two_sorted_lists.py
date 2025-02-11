# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        stack = ListNode()

        while list1 or list2:
            if list1.val > list2.val:
                stack.next = list1
                list1 = list1.next
            else:
                stack.next = list2
                list2 = list2.next
            stack = stack.next

        stack.next = list1 if list1 else list2

        return stack.next


    @staticmethod
    def list_to_linkedlist(lst):
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

if __name__ == '__main__':

    list_1 = [1, 2, 4]
    list_2 = [1, 3, 4]
    expected_answer = [1,1,2,3,4,4]
    s = Solution()
    l1 = s.list_to_linkedlist(list_1)
    l2 = s.list_to_linkedlist(list_2)
    answer = s.mergeTwoLists(l1,l2)


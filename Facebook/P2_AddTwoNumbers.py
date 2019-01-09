
'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        cur_node = root
        prev_node = None

        carry_val = 0
        while l1 and l2:
            '''
            Add up curr nodes
            '''
            cur_sum = l1.val + l2.val + carry_val
            cur_node.val = cur_sum % 10
            carry_val = cur_sum / 10

            cur_node.next = ListNode(0)
            prev_node = cur_node
            cur_node = cur_node.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            cur_sum = l1.val + carry_val
            cur_node.val = cur_sum % 10
            carry_val = cur_sum / 10

            cur_node.next = ListNode(0)
            prev_node = cur_node
            cur_node = cur_node.next
            l1 = l1.next

        while l2:
            cur_sum = l2.val + carry_val
            cur_node.val = cur_sum % 10
            carry_val = cur_sum / 10

            cur_node.next = ListNode(0)
            prev_node = cur_node
            cur_node = cur_node.next
            l2 = l2.next

        if carry_val:
            cur_node.val = carry_val
            return root
        else:
            prev_node.next = None

        return root
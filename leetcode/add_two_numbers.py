# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':

        # Use a dummy root_node. Result will be a next node.
        root_node = ListNode(None)

        # We will override node variable in the while loop. We don't want to override root_node
        node = root_node

        add_one = 0

        while l1 or l2 or add_one:
            # Create a new ListNode
            node.next = ListNode(None)

            # Reassing node variable
            node = node.next

            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add_one

            # Can be done in one line with divmod()
            # add_one, value = divmod(value, 10)

            if value >= 10:
                value = value % 10
                add_one = 1
            else:
                add_one = 0

            node.val = value

            # Update l1 and l2 to the following nodes
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return root_node.next

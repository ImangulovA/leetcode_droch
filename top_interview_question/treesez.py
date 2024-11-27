# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True

            # The current node's value must be within the range [low, high]
            if not (low < node.val < high):
                return False

            # Recursively validate the left and right subtrees
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root)


from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        # Initialize a queue with the left and right children of the root
        queue = deque([(root.left, root.right)])

        while queue:
            left, right = queue.popleft()

            # If both nodes are None, continue to the next pair
            if not left and not right:
                continue
            # If only one of the nodes is None or the values are not equal, return False
            if not left or not right or left.val != right.val:
                return False

            # Enqueue the children in a mirrored order
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        # If we finished processing all pairs, the tree is symmetric
        return True
# https://www.geeksforgeeks.org/deque-in-python/


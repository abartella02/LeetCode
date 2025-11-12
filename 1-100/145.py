from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def traverse(_root):
            if _root is None:
                return
            traverse(_root.left)
            traverse(_root.right)
            arr.append(_root.val)

        traverse(root)
        return arr

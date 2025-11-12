from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def traverse(_root):
            if _root.left is not None:
                arr.append(_root.left)
                traverse(_root.left)
            if _root.right is not None:
                arr.append(_root.right)
                traverse(_root.right)
            if _root.left is None and _root.right is None:
                return None

        traverse(root)
        print(arr)

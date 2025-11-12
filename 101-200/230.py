"""
Kth smallest element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
of all the values of the nodes in the tree.
"""

from typing import *
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallestLoop(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal using while loop
        # left, root, right

        stack = deque()

        i = 0
        node = root
        node_k = None
        while (node or stack) and i < k:
            while node:
                stack.append(node)
                node = node.left

            node_k = stack.pop()
            node = node_k.right
            i += 1

        return node_k.val

    def kthSmallestRecursive(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal using recursion

        i = 0
        node_k = None

        def inOrder(node):
            nonlocal node_k
            nonlocal i
            if node is None or node_k:
                return

            inOrder(node.left)
            i += 1
            if i == k:
                node_k = node.val
                return

            inOrder(node.right)

        inOrder(root)

        return node_k

"""
Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root
with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in tree and all of this
node's descendants. The tree `tree` could also be considered as a subtree of itself.

i.e. find the subtree
  1
 | \
3   5
in the following trees

   true            false
    2                2
   | \              | \
  1   1            1   1
 | \              | \
3   5            3   5
                      \
                       1
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs_compareNodes(node, subnode):
            # do dfs while comparing each node
            if node is None and subnode is None:
                # if both nodes are None, they terminate at the same time
                # which means they're identical so far
                return True

            if (node is None) ^ (subnode is None):
                # if only one node is None
                # they are not identical
                return False

            if node.val == subnode.val:  # nodes are identical
                return dfs_compareNodes(node.left, subnode.left) and dfs_compareNodes(
                    node.right, subnode.right
                )
            return False  # nodes are not none but not identical

        def dfs(node, subnode):
            # do dfs and run comparenodes on each node
            if subnode is None:
                return True

            if node is None:
                return False

            if dfs_compareNodes(node, subnode):
                return True

            return dfs(node.left, subnode) or dfs(node.right, subnode)

        return dfs(root, subRoot)

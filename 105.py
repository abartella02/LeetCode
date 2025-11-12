"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a
binary tree and inorder is the inorder traversal of the same tree, construct and return
the binary tree.
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Key concepts:
        - preorder always has the next node at the front of the list
        - inorder shows how many nodes (leafs) are on the left and right branches of a given node
            - i.e. preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
              root node is 3
              inorder says left=[9], right=[15, 20, 7]
              9 is next in preorder, left of 3 is just 9 since len(left) == 1
              20 is next in preorder
              right of 3 is 20, look at inorder --> left = [15], right = [7]
              15 is next in preorder, left of 20 is just 15
              7 is next in preorder, right of 20 is just 7
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def bisect(arr: List, x: int) -> Tuple[List[int], List[int]]:
            """Split the array about x (x not included in result)"""
            n = len(arr)
            i = arr.index(x)

            if i < n - 1:
                return arr[:i], arr[i + 1 :]
            return arr[:i], []

        def construct(preorder: List, inorder: List) -> Optional[TreeNode]:
            """Construct a node and recursively construct its children"""
            if inorder:  # bisect produces empty array when end of branch reached
                root_val = preorder.pop(0)  # next node in preorder
                root = TreeNode(val=root_val)  # create node

                left, right = bisect(inorder, root_val)  # split inorder about root
                root.left = construct(
                    preorder, left
                )  # construct left side using left inorder
                root.right = construct(
                    preorder, right
                )  # construct right side using right inorder

                return root

        return construct(preorder, inorder)

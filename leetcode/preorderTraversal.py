# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(
            self, root: Optional[TreeNode]) -> List[int]:
        return preorder(root)


def preorder(root):
    ans = []

    def helper(node):
        if node:
            ans.append(node.val)
            helper(node.left)
            helper(node.right)

    helper(root)
    return ans

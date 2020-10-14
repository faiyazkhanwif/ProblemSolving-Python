# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#One of the hardest BST problems tried. Done successfully
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        elem = []
        self.ans = 0

        def code(root):
            if root.val == None:
                return
            val = root.val
            elem.append(val)
            if root.left:
                l = code(root.left)
            if root.right:
                r = code(root.right)
            if not root.left and not root.right:
                value = 0
                # print(elem)
                elem1 = elem.copy()
                for i in range(len(elem1)):
                    digit = elem1.pop()
                    # print(digit)
                    if digit == 1:
                        value = value + pow(2, i)
                # print (value)
                self.ans += value
            elem.pop()

        code(root)
        return self.ans

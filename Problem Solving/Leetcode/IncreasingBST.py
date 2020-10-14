#stack solution
def increasingBST(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None
    stack = []
    temp = x = root
    i = 0
    while stack or temp:
        if temp:
            stack.append(temp)
            temp = temp.left
        else:
            node = stack.pop()
            if i == 0:
                root = x = node
                i += 1
            else:
                x.right = node
                x = node
                x.left = None
            temp = node.right
    return root


#recursive implementation
def increasingBST(self, root, tail=None):
    # if this null node was a left child, tail is its parent
    # if this null node was a right child, tail is its parent's parent
    if not root: return tail

    # recursive call, traversing left while passing in the current node as tail
    res = self.increasingBST(root.left, root)

    # we don't want the current node to have a left child, only a single right child
    root.left = None

    # we set the current node's right child to be tail
    # what is tail? this part is important
    # if the current node is a left child, tail will be its parent
    # else if the current node is a right child, tail will be its parent's parent
    root.right = self.increasingBST(root.right, tail)

    # throughout the whole algorithm, res is the leaf of the leftmost path in the original tree
    # its the smallest node and thus will be the root of the modified tree
    return res


from treeNode import TreeNode

current = head = TreeNode(3)
current.left, current.right = TreeNode(9), TreeNode(20)
current = current.right
current.left, current.right = TreeNode(15), TreeNode(7)

def minDepth(root):
    if not root:    return 0
    if not root.left:
        return minDepth(root.right) + 1
    if not root.right:
        return minDepth(root.left) + 1
    return min(minDepth(root.left), minDepth(root.right)) + 1
print(minDepth(head))



from treeNode import TreeNode

current = head = TreeNode(3)
current.left, current.right = TreeNode(9), TreeNode(20)
current = current.right
current.left, current.right = TreeNode(15), TreeNode(7)


def maxDepth(root):
    counter = 0
    def findDepth(root, counter):
        if not root:
            return counter
        return max(findDepth(root.left, counter+1), findDepth(root.right, counter+1))
    return findDepth(root, counter)

print(maxDepth(head))
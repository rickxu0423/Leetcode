from treeNode import TreeNode

current = head = TreeNode(3)
current.left, current.right = TreeNode(9), TreeNode(20)
current = current.right
current.left, current.right = TreeNode(15), TreeNode(7)


def minDepth(root):
    if not root:    return 0
    else:   queue = [(1, root)]
    while queue:
        depth, root = queue.pop(0)
        children = [root.left, root.right]
        if not any(children):
            return depth
        for c in children:
            if c:
                queue.append((depth+1, c))
print(minDepth(head))
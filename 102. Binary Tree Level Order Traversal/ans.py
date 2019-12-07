from treeNode import TreeNode

current = head = TreeNode(3)
current.left, current.right = TreeNode(9), TreeNode(20)
current = current.right
current.left, current.right = TreeNode(15), TreeNode(7)


def levelOrder(root):
    if not root:    return []
    result, queue= [], []
    queue.append(root)
    while queue:
        level = []
        tem = []
        while queue:
            stuff = queue.pop(0)
            level.append(stuff.val)
            if stuff.left:  tem.append(stuff.left)
            if stuff.right: tem.append(stuff.right)
        result.append(level)
        queue += tem
    return result

print(levelOrder(head))
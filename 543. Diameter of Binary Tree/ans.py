from treeNode import TreeNode

current = head = TreeNode(3)
current.left, current.right = TreeNode(9), TreeNode(20)
current = current.right
current.left, current.right = TreeNode(15), TreeNode(7)

def diameterOfBinaryTree(root):
    ans = 1

    def dfs(node):
        nonlocal ans
        if not node: return 0
        left = dfs(node.left)
        right = dfs(node.right)
        ans = max(ans, left + right + 1)
        return max(left, right) + 1
    dfs(root)
    return ans - 1

print(diameterOfBinaryTree(head))
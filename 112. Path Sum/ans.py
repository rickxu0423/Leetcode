
def hasPathSum(root, sum):
    if not root: return False

    def dfs(node, val):
        if not node: return False
        if not node.right and not node.left:
            if val + node.val == sum: return True
            else: return False
        return dfs(node.left, val + node.val) or dfs(node.right, val + node.val)
        
    return dfs(root, 0)



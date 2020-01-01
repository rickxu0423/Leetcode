function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

var head = current = new TreeNode(3);
[current.left, current.right] = [new TreeNode(4), new TreeNode(5)];
current = current.right;
[current.left, current.right] = [new TreeNode(10), new TreeNode(12)];

var diameterOfBinaryTree = function(root) {
    var ans = 1;
    dfs(root);
    return ans - 1;
    
    function dfs(node) {
        if (!node) return 0;
        let left = dfs(node.left);
        let right = dfs(node.right);
        ans = Math.max(ans, left + right + 1);
        return Math.max(left, right) + 1;
    }
};

console.log(diameterOfBinaryTree(head))
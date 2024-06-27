class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.create_tree(self.inorder_traversal(root))


    def inorder_traversal(self, root: TreeNode):
        if root is None:
            return []
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)
            
    def create_tree(self, sorted_tree: List):
        if len(sorted_tree) == 0:
            return None
        return TreeNode(sorted_tree[len(sorted_tree) // 2], self.create_tree(sorted_tree[:len(sorted_tree) // 2]), self.create_tree(sorted_tree[len(sorted_tree) // 2 + 1:]))
    
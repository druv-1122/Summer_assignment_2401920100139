class Solution:
    def invertTree(self, root):
        if root is None:
            return None

        current_node = root

        left_subtree = current_node.left
        right_subtree = current_node.right

        current_node.left = right_subtree
        current_node.right = left_subtree

        updated_left = current_node.left
        updated_right = current_node.right

        if updated_left is not None:
            self.invertTree(updated_left)

        if updated_right is not None:
            self.invertTree(updated_right)

        final_root = current_node

        return final_root

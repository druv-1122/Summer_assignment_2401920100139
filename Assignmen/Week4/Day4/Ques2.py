class Solution:
    def diameterOfBinaryTree(self, root):
        self.maximum_diameter = 0

        def find_height(node):
            if node is None:
                return 0

            left_height = find_height(node.left)
            right_height = find_height(node.right)

            current_diameter = left_height + right_height

            if current_diameter > self.maximum_diameter:
                self.maximum_diameter = current_diameter

            current_height = max(left_height, right_height) + 1
            return current_height

        find_height(root)

        return self.maximum_diameter

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        current_node = root

        while current_node is not None:
            current_node_value = current_node.val

            first_node_value = p.val
            second_node_value = q.val

            is_first_node_smaller = first_node_value < current_node_value
            is_second_node_smaller = second_node_value < current_node_value

            is_first_node_greater = first_node_value > current_node_value
            is_second_node_greater = second_node_value > current_node_value

            if is_first_node_smaller and is_second_node_smaller:
                next_node_to_visit = current_node.left
                current_node = next_node_to_visit

            elif is_first_node_greater and is_second_node_greater:
                next_node_to_visit = current_node.right
                current_node = next_node_to_visit

            else:
                lowest_common_ancestor = current_node
                return lowest_common_ancestor

        result = None
        return result

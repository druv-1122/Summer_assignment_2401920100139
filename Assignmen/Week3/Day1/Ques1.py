class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False

        visited_nodes = set()
        current_node = head

        while current_node is not None:
            if current_node in visited_nodes:
                return True
            else:
                visited_nodes.add(current_node)

            if current_node.next is None:
                return False

            current_node = current_node.next

        return False

class Node:
    def __init__(self, data):
        self.data = data
        self.next_ptr = None


# Create nodes
node1 = Node("test1")
node2 = Node("test2")
node3 = Node("test3")

# Link nodes
node1.next_ptr = node2
node2.next_ptr = node3
node3.next_ptr = node1  # circular link

# Traverse nodes
current = node1
visited = set()  # to prevent infinite loop in circular list

while current is not None and current not in visited:
    print(current.data, current.next_ptr)
    visited.add(current)
    current = current.next_ptr

print()

class Node:
    def __init__(self, data: str):
        self.data = data
        self.next_ptr = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data: str):
        new_node = Node(data)
        new_node.next_ptr = self.top  # link new node to previous top
        self.top = new_node           # update top to new node

    def pop(self) -> str:
        if self.top is None:
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next_ptr
        return popped_node.data
    
    def peek(self) -> str:
        if self.top is None:
            raise IndexError("peek from empty stack")
        return self.top.data
    
    def isFull(self) -> bool:
        return False  # stack will never be full in this context

    def isEmpty(self) -> bool:
        return self.top is None

def main():
    node1 = Node("test1")
    node2 = Node("test2")
    node3 = Node("test3")
    node4 = Node("test4")
    nodes = [node1, node2, node3, node4]

    stack = Stack()
    for node in nodes:
        stack.push(node.data)
        print(f"Pushed: {node.data}")

    print("Peek:", stack.peek())

    while not stack.isEmpty():
        print("Popped:", stack.pop())

if __name__ == "__main__":
    main()
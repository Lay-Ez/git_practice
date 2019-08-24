from Nodes_introduction import Node

class Stack:
    def __init__(self, limit=1000):
        self.top_item = top_item
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.size < self.limit:
            new_item = Node(value)
            new_item.set_next_node(self.top_item)
            self.top_item = new_item
            self.size += 1
        else:
            print("stack out of space")

    def pop(self):
        if not self.is_empty() > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.next_node
            self.size -= 1
            return item_to_remove.value
        else:
            print("stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("stack is empty")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

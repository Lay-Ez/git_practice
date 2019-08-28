from node import Node

class Queue:

    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def peek(self):
        if not self.is_empty():
            return self.head.get_value()
        print("Nothing to see here!")

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size != None:
            return self.max_size > self.size
        return True

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding {} to the queue!".format(str(item_to_add.get_value())))
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")

    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print("Removing {} from the queue!".format(str(item_to_remove.get_value())))
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        print("This queue is empty!")

class TreeNode:
    def __init__(self, value):
        print("initializing node...")
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding {}".format(child_node.value))
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing {} from {}".format(child_node.value, self.value))
        self.children = [child for child in self.children if child != child_node]

    def traverse(self):
        print("Traversing...")
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


root = TreeNode("CEO")
first_child = TreeNode("Boss1")
second_child = TreeNode("Boss2")

root.add_child(first_child)
root.add_child(second_child)

first_child_1 = TreeNode("HeadManager1")
first_child_2 = TreeNode("HeadManager2")
first_child_3 = TreeNode("HeadManager3")
first_child_4 = TreeNode("HeadManager4")

first_child.add_child(first_child_1)
first_child.add_child(first_child_2)
first_child.add_child(first_child_3)

second_child.add_child(first_child_4)

root.traverse()

root.remove_child(second_child)

root.traverse()

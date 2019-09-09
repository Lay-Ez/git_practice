from random import randint

class MinHeap:

    def __init__(self):

        self.heap_list = [None]
        self.count = 0

#   Helper methods

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

# End of helper methods

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        left_child = self.heap_list[self.left_child_idx(idx)]
        right_child = self.heap_list[self.right_child_idx(idx)]
        if left_child < right_child:
            print("Left child is smaller")
            return self.left_child_idx(idx)
        else:
            print("Right child is smaller")
            return self.right_child_idx(idx)

    def add(self, element):
        #print("Adding {} to {}".format(element, self.heap_list))
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        #print("Restoring the heap property...")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent > child:
                print("Swapping {} with {}".format(parent, child))
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        #print("Heap restored {}".format(self.heap_list))

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None
        min = self.heap_list[1]
        print("Removing: {} from {}".format(min, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.heap_list[self.count] = min
        self.heap_list.pop()
        self.count -= 1
        print("Last element moved to first: {}".format(self.heap_list))
        self.heapify_down()
        return min

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            #print("Heapifying down!")
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]
            if parent > child:
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent
            idx = smaller_child_idx
        #print("Heap Restored! {}".format(self.heap_list))


my_heap = MinHeap()

for i in range(1, 100):
    my_heap.add(randint(1, 100))

while True:
    user_input = input("")
    my_heap.retrieve_min()

from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:

    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(self.array_size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for item in list_at_array:
            if item[0] == key:
                item[1] = value
                return
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if item[0] == key:
                return item[1]
        return None

    def remove(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if item[0] == key:
                item[1] = None
        return




blossom = HashMap(len(flower_definitions))

for item in flower_definitions:
    blossom.assign(item[0], item[1])



user_input = str(input("\n What flower definition do you want to know?\n (Enter 'opt' to see the options)\n"))

if blossom.retrieve(user_input) != None:
    print("\n  Meaning of {} is {}\n".format(user_input, blossom.retrieve(user_input)))
elif blossom.retrieve(user_input) == None and user_input != "opt":
    print("\n Sorry, there is no such flower in collection\n")
#elif user_input == "opt":
    #user_input =  str(input("\n (Enter 'exit' to exit)\n (Enter 'add' to add flower to library)\n (Enter 'remove' to remove item)\n (Enter 'print' to see all items)\n"))


while True:
    if user_input != "opt":
        user_input = str(input("\n Any other flower?\n (Enter options to see the options)\n"))

    if user_input == "opt":
        user_input =  str(input("\n (Enter 'exit' to exit)\n (Enter 'add' to add flower to library)\n (Enter 'remove' to remove item)\n (Enter 'print' to see all items)\n (Enter 'cont' to continue viewing)\n"))
        if user_input == "exit":
            print("\n\n\n---Bye Bye!---\n")
            break
        if user_input == "add":
            flower_to_add = str(input("\n What flower do you want to add?\n"))
            meaning_to_add = str(input("\n What's the meaning of that flower?\n"))
            blossom.assign(flower_to_add, meaning_to_add)
            flower_definitions.append([flower_to_add, meaning_to_add])
            print("\n Added {} to collection\n".format(flower_to_add))
            continue
        if user_input == "remove":
            item_to_remove = str(input("\n What flower do you want to remove?\n"))
            blossom.remove(item_to_remove)
            print("\n  {} removed from collection\n".format(item_to_remove))
            continue
        if user_input == "print":
            print("\n Here are all items in the collection\n")
            for lst in blossom.array:
                for item in lst:
                    if item[1] != None:
                        print(item)
            continue
        if user_input == "cont":
            continue

    if blossom.retrieve(user_input) != None:
        print("\n  Meaning of {} is {}\n".format(user_input, blossom.retrieve(user_input)))
        continue

    else:
        print("\n Sorry, there is no such flower in collection\n")
        continue

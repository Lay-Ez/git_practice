class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(self.array_size)]

    def hash(self, key, count_collisions = 0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value == None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] != key:
            number_collisions = 1

            while current_array_value[0] != key and number_collisions < self.array_size:
                new_hash_code = self.hash(key, number_collisions)
                new_array_index = self.compressor(new_hash_code)
                current_array_value = self.array[new_array_index]

                if current_array_value is None:
                    self.array[new_array_index] = [key, value]
                    return

                if current_array_value[0] == key:
                    self.array[new_array_index] = [key, value]
                    return

                if current_array_value[0] != key:
                    number_collisions += 1

            print("---Not enough space to add '{}'---".format(key))



    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]
        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        if possible_return_value[0] != key:
            retrieval_collisions = 1
            while possible_return_value[0] != key and retrieval_collisions < self.array_size:
                new_hash_code = self.hash(key, retrieval_collisions)
                new_array_index = self.compressor(new_hash_code)
                possible_return_value = self.array[new_array_index]

                if possible_return_value[0] == key:
                    return possible_return_value[1]

                if possible_return_value is None:
                    return None

                if possible_return_value[0] != key:
                    retrieval_collisions += 1

            return None

    def remove(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]
        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            self.array[array_index] = None
            return

        if possible_return_value[0] != key:
            retrieval_collisions = 1
            while possible_return_value[0] != key and retrieval_collisions < self.array_size:
                new_hash_code = self.hash(key, retrieval_collisions)
                new_array_index = self.compressor(new_hash_code)
                possible_return_value = self.array[new_array_index]

                if possible_return_value[0] == key:
                    self.array[new_array_index] = None
                    return

                if possible_return_value is None:
                    return None

                if possible_return_value[0] != key:
                    retrieval_collisions += 1

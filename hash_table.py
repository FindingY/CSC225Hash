"""CSC 225 - Hash table starter. Complete the TODO sections."""

# These prime sizes are provided; you do not need to test for prime numbers.
SIZES = [11, 23, 47, 97, 197, 397]


class HashTable:
    def __init__(self, method="linear", hash_method="mod"):
        self.method = method           # linear, quadratic, or chaining
        self.hash_method = hash_method # mod or digit
        self.capacity = 11
        self.count = 0

        if method == "chaining":
            # Each position must have its OWN list.
            # [[]] * 11 would repeat references to the SAME list.
            self.table = [[] for i in range(self.capacity)]
        else:
            self.table = [None] * self.capacity

    def hash_key(self, key):
        # These two hash functions are already provided.
        if self.hash_method == "mod":
            return key % self.capacity
        total = 0
        for digit in str(abs(key)):
            total += int(digit)
        return total % self.capacity

    def insert(self, key):
        # TODO 1: Do not insert a duplicate. Use search() to check.
        # TODO 2: Check whether one more key would exceed the limit:
        #         linear: 0.70, quadratic: 0.50, chaining: 0.75.
        #         If so, call resize() BEFORE inserting the new key.
        #         Do this only after completing Milestone 4.
        # TODO 3: Use hash_key(key) to find the starting position.
        #         linear: try (start + i) % capacity
        #         quadratic: try (start + i*i) % capacity
        #         chaining: append to the list at the start position
        # TODO 4: Increase count after inserting successfully.
        pass

    def search(self, key):
        # TODO: Return True if key is stored, and False otherwise.
        # Use the same positions as insert() for each method.
        # In open addressing, stop at an empty position or after
        # capacity attempts. No deletion is required.
        pass

    def resize(self):
        # TODO (Milestone 4):
        # 1. Save your old table.
        # 2. Change capacity to the next value in SIZES.
        # 3. Make a new empty table of the correct kind.
        # 4. Set count to 0.
        # 5. Insert each old value again using insert().
        #    For chaining, remember each position is a LIST.
        # Do not just copy old values into the same positions.
        pass

    def show(self):
        print("\nMethod:", self.method, "| Hash:", self.hash_method)
        print("Size:", self.capacity, "| Values:", self.count)
        print("Load factor:", round(self.count / self.capacity, 2))
        for i in range(self.capacity):
            print(i, ":", self.table[i])

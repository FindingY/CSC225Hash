"""CSC 225 hash table starter.

Implement the TODO methods milestone by milestone. Do NOT use dict, set,
or built-in hash() to implement your table.
"""

from hash_functions import hash_mod, hash_digit_sum


class HashTable:
    """A table storing unique integer keys.

    Public interface (keep these signatures and return types):
      insert(key) -> bool: True if inserted, False if duplicate/full.
      search(key) -> bool: True if found, otherwise False.
      display() -> None: print all indices and contents.
      load_factor() -> float
      get_values() -> list[int]
      resize() -> None: grow and rehash all existing keys.
      statistics() -> None: print capacity, count, load factor, etc.

    Collision strategies: 'linear', 'quadratic', 'chaining'.
    Hash functions: 'mod', 'digit_sum'.
    """

    THRESHOLDS = {"linear": 0.70, "quadratic": 0.50, "chaining": 0.75}

    def __init__(self, capacity: int = 11,
                 collision_method: str = "linear",
                 hash_method: str = "mod") -> None:
        # Milestone 1: validate these options, save attributes, initialize
        # self.table appropriately, and initialize self.count to zero.
        # Open addressing: [None] * capacity
        # Chaining: [[] for _ in range(capacity)] (avoid [[]] * capacity)
        raise NotImplementedError("Milestone 1: implement __init__")

    def _hash(self, key: int) -> int:
        # Milestone 1: delegate to one of the provided functions, passing
        # the current self.capacity. Do not copy their formulas here.
        raise NotImplementedError("Milestone 1: implement _hash")

    def display(self) -> None:
        # Milestone 1: print every array index and its contents.
        raise NotImplementedError("Milestone 1: implement display")

    def insert(self, key: int) -> bool:
        # Milestones 2-3: implement insertion, duplicate prevention, and
        # collision handling for each selected method.
        # Milestone 5: BEFORE adding a new key, check projected load factor;
        # resize if it exceeds the method's threshold. During rehashing,
        # avoid recursively triggering resize or corrupting self.count.
        # Return True only for a newly inserted value.
        raise NotImplementedError("Milestone 2/3: implement insert")

    def search(self, key: int) -> bool:
        # Milestones 2-3: follow the same probe sequence as insertion, or
        # search the appropriate chain. Limit probe attempts to capacity.
        raise NotImplementedError("Milestone 2/3: implement search")

    def load_factor(self) -> float:
        # Milestone 4: number of stored values / current capacity.
        raise NotImplementedError("Milestone 4: implement load_factor")

    def statistics(self) -> None:
        # Milestone 4: print strategy, hash method, capacity, number of
        # elements, and load factor.
        raise NotImplementedError("Milestone 4: implement statistics")

    def get_values(self) -> list[int]:
        # Milestone 5: return a FLAT list of stored keys (all chains must
        # be flattened); no None entries.
        raise NotImplementedError("Milestone 5: implement get_values")

    @staticmethod
    def _is_prime(number: int) -> bool:
        # Milestone 5: return whether number is prime.
        raise NotImplementedError("Milestone 5: implement _is_prime")

    def resize(self) -> None:
        # Milestone 5: choose the smallest prime >= 2*old_capacity + 1,
        # allocate a fresh table, and REHASH every existing value.
        raise NotImplementedError("Milestone 5: implement resize")

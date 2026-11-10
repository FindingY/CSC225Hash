"""Run with: python -m unittest tests.test_milestone2 -v"""

import unittest
from hash_table import HashTable


class LinearProbingTests(unittest.TestCase):
    def test_collision_and_wraparound(self):
        table = HashTable()
        for key in [10, 21, 32, 43, 54]:
            self.assertTrue(table.insert(key))
        self.assertEqual(table.table[10], 10)
        self.assertEqual(table.table[0:4], [21, 32, 43, 54])
        self.assertEqual(table.count, 5)

    def test_search_and_duplicate(self):
        table = HashTable()
        for key in [10, 21, 32]:
            table.insert(key)
        self.assertTrue(table.search(21))
        self.assertFalse(table.search(999))
        self.assertFalse(table.insert(21))
        self.assertEqual(table.count, 3)

    def test_full_table_does_not_loop(self):
        # Fixed-capacity behavior is tested before Milestone 5.
        table = HashTable(capacity=5)
        for value in range(5):
            self.assertTrue(table.insert(value))
        self.assertFalse(table.insert(99))
        self.assertEqual(table.count, 5)


if __name__ == "__main__":
    unittest.main()

"""Run with: python -m unittest tests.test_milestone1 -v"""

import io
import unittest
from contextlib import redirect_stdout
from hash_functions import hash_mod, hash_digit_sum
from hash_table import HashTable


class Milestone1Tests(unittest.TestCase):
    def test_provided_hash_functions(self):
        self.assertEqual(hash_mod(21, 11), 10)
        self.assertEqual(hash_mod(32, 11), 10)
        self.assertEqual(hash_digit_sum(10000, 11), 1)
        self.assertEqual(hash_digit_sum(-100, 11), 1)

    def test_initialization_and_hash_selection(self):
        table = HashTable()
        self.assertEqual(table.capacity, 11)
        self.assertEqual(table.count, 0)
        self.assertEqual(len(table.table), 11)
        self.assertTrue(all(item is None for item in table.table))
        self.assertEqual(table._hash(21), 10)
        other = HashTable(hash_method="digit_sum")
        self.assertEqual(other._hash(10000), 1)

    def test_chaining_has_independent_buckets(self):
        table = HashTable(collision_method="chaining")
        self.assertEqual(table.table, [[] for _ in range(11)])
        self.assertIsNot(table.table[0], table.table[1])

    def test_display_shows_every_index(self):
        table = HashTable()
        capture = io.StringIO()
        with redirect_stdout(capture):
            table.display()
        output = capture.getvalue()
        for i in range(11):
            self.assertIn(str(i), output)


if __name__ == "__main__":
    unittest.main()

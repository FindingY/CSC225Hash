"""Run with: python -m unittest tests.test_milestone3 -v"""

import unittest
from hash_table import HashTable


class CollisionMethodsTests(unittest.TestCase):
    def test_quadratic_expected_positions(self):
        table = HashTable(collision_method="quadratic")
        for key in [10, 21, 32, 43, 54]:
            self.assertTrue(table.insert(key))
        for index, key in [(10, 10), (0, 21), (3, 32), (8, 43), (4, 54)]:
            self.assertEqual(table.table[index], key)
            self.assertTrue(table.search(key))
        self.assertFalse(table.search(999))

    def test_chaining_expected_bucket(self):
        table = HashTable(collision_method="chaining")
        for key in [10, 21, 32, 43, 54]:
            self.assertTrue(table.insert(key))
        self.assertEqual(table.table[10], [10, 21, 32, 43, 54])
        self.assertTrue(table.search(43))
        self.assertFalse(table.search(999))
        self.assertFalse(table.insert(21))
        self.assertEqual(table.count, 5)

    def test_digit_sum_hash_for_three_methods(self):
        for method in ["linear", "quadratic", "chaining"]:
            with self.subTest(method=method):
                table = HashTable(collision_method=method,
                                  hash_method="digit_sum")
                for key in [10, 100, 1000, 10000]:
                    self.assertTrue(table.insert(key))
                self.assertTrue(all(table.search(key)
                                    for key in [10, 100, 1000, 10000]))


if __name__ == "__main__":
    unittest.main()

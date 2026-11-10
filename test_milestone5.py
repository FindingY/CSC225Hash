"""Run with: python -m unittest tests.test_milestone5 -v"""

import unittest
from hash_table import HashTable


class ResizingTests(unittest.TestCase):
    def test_thresholds_and_preserved_values(self):
        cases = [
            ("linear", list(range(8))),
            ("quadratic", [10, 21, 32, 43, 54, 65]),
            ("chaining", list(range(9))),
        ]
        for method, values in cases:
            with self.subTest(method=method):
                table = HashTable(collision_method=method)
                for key in values:
                    self.assertTrue(table.insert(key))
                self.assertEqual(table.capacity, 23)
                self.assertEqual(table.count, len(values))
                self.assertTrue(all(table.search(key) for key in values))

    def test_repeated_resizes(self):
        for method in ["linear", "quadratic", "chaining"]:
            with self.subTest(method=method):
                table = HashTable(collision_method=method)
                for key in range(50):
                    self.assertTrue(table.insert(key))
                self.assertGreater(table.capacity, 23)
                self.assertEqual(table.count, 50)
                self.assertTrue(all(table.search(key) for key in range(50)))

    def test_no_resize_for_duplicate(self):
        table = HashTable(collision_method="quadratic")
        for key in [0, 1, 2, 3, 4]:
            table.insert(key)
        self.assertFalse(table.insert(4))
        self.assertEqual(table.capacity, 11)
        self.assertEqual(table.count, 5)


if __name__ == "__main__":
    unittest.main()

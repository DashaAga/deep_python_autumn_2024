import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def test_add_custom_list(self):
        self.assertEqual(CustomList([5, 1, 3, 7]) +
                         CustomList([1, 2, 7]),
                         CustomList([6, 3, 10, 7]))

    def test_add_list(self):
        self.assertEqual(CustomList([10]) + [2, 5], CustomList([12, 5]))

    def test_radd_list(self):
        self.assertEqual([2, 5] + CustomList([10]), CustomList([12, 5]))

    def test_add_number(self):
        self.assertEqual(CustomList([2, 5]) + 10, CustomList([12, 15]))

    def test_radd_number(self):
        self.assertEqual(10 + CustomList([2, 5]), CustomList([12, 15]))

    def test_sub_custom_list(self):
        self.assertEqual(CustomList([5, 1, 3, 7]) -
                         CustomList([1, 2, 7]),
                         CustomList([4, -1, -4, 7]))

    def test_sub_list(self):
        self.assertEqual(CustomList([10]) - [2, 5], CustomList([8, -5]))

    def test_rsub_list(self):
        self.assertEqual([2, 5] - CustomList([10]), CustomList([-8, 5]))

    def test_sub_number(self):
        self.assertEqual(CustomList([2, 5]) - 10, CustomList([-8, -5]))

    def test_rsub_number(self):
        self.assertEqual(10 - CustomList([2, 5]), CustomList([8, 5]))

    def test_str(self):
        self.assertEqual(str(CustomList([1, 2, 3])), "[1, 2, 3] (sum: 6)")

    def test_eq(self):
        self.assertTrue(CustomList([1, 2, 3]) == CustomList([6]))
        self.assertTrue(CustomList([1, 2, 3]) == CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) == CustomList([4, 5]))

    def test_ne(self):
        self.assertTrue(CustomList([1, 2, 3]) != CustomList([7]))
        self.assertFalse(CustomList([1, 2, 3]) != CustomList([1, 2, 3]))

    def test_lt(self):
        self.assertTrue(CustomList([1, 2, 3]) < CustomList([10]))
        self.assertFalse(CustomList([1, 2, 3]) < CustomList([1, 2, 3]))

    def test_le(self):
        self.assertTrue(CustomList([1, 2, 3]) <= CustomList([6]))
        self.assertTrue(CustomList([1, 2, 3]) <= CustomList([10]))
        self.assertFalse(CustomList([1, 2, 3]) <= CustomList([5]))

    def test_gt(self):
        self.assertTrue(CustomList([4, 5]) > CustomList([3]))
        self.assertFalse(CustomList([4, 5]) > CustomList([9]))

    def test_ge(self):
        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([6]))
        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([5]))
        self.assertFalse(CustomList([1, 2, 3]) >= CustomList([7]))

    def test_custom_list_addition_different_lengths(self):
        self.assertEqual(CustomList([1, 2]) +
                         CustomList([3, 4, 5]),
                         CustomList([4, 6, 5]))

    def test_custom_list_subtraction_different_lengths(self):
        self.assertEqual(CustomList([1, 2, 3]) -
                         CustomList([3, 4]),
                         CustomList([-2, -2, 3]))

    def test_empty_custom_list(self):
        self.assertEqual(CustomList([]) +
                         CustomList([1, 2]),
                         CustomList([1, 2]))
        self.assertEqual(CustomList([1, 2]) -
                         CustomList([]),
                         CustomList([1, 2]))
        self.assertEqual(CustomList([1, 2]) +
                         CustomList([]),
                         CustomList([1, 2]))
        self.assertEqual(CustomList([]) -
                         CustomList([1, 2]),
                         CustomList([-1, -2]))


if __name__ == '__main__':
    unittest.main()

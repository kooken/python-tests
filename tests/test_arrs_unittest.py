import unittest
from utils import arrs


class TestGet(unittest.TestCase):

    def test_returns_value_at_index(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "default"), 2)

    def test_returns_default_for_empty_list(self):
        self.assertEqual(arrs.get([], 0, "default"), "default")

    def test_returns_value_at_first_index(self):
        self.assertEqual(arrs.get([10, 20, 30], 0, "default"), 10)

    def test_returns_value_at_last_index(self):
        self.assertEqual(arrs.get([10, 20, 30], 2, "default"), 30)

    def test_returns_default_when_index_out_of_bounds(self):
        self.assertEqual(arrs.get([1, 2, 3], 5, "default"), "default")

    def test_returns_default_for_negative_index(self):
        self.assertEqual(arrs.get([1, 2, 3], -1, "default"), "default")

    def test_returns_none_as_default(self):
        self.assertIsNone(arrs.get([1, 2, 3], 10))


class TestMySlice(unittest.TestCase):

    def test_with_start_and_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])

    def test_with_start_only(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_with_no_args(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], None), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(arrs.my_slice([]), [])

    def test_with_end_beyond_length(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, 100), [1, 2, 3])

    def test_with_negative_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2), [3, 4])

    def test_with_negative_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, -1), [1, 2, 3])

    def test_entire_list(self):
        self.assertEqual(arrs.my_slice([1, 2, 3]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()

import unittest
from flatter import flatter


class FlatterTestCase(unittest.TestCase):
    def test_flat_list(self):
        self.assertEqual(flatter([[1, [2, [3, [4, 5]]]]]), [1, 2, 3, 4, 5])

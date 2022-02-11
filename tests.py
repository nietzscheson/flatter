import unittest
from flatter import flatter


class FlatterTestCase(unittest.TestCase):
    def test_flat_list(self):
        self.assertEqual(flatter([[1, [2, [3, [4, 5]]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatter([[0, 1], [2, 3]]), [0, 1, 2, 3])
        self.assertEqual(flatter([0, [1], 2, 3]), [0, 1, 2, 3])
        self.assertEqual(flatter([-1, 0, [1], 2, 3]), [-1, 0, 1, 2, 3])
        self.assertEqual(flatter(["a", 0, [1], 2, 3]), ["a", 0, 1, 2, 3])
        self.assertEqual(
            flatter([[0, 1], [[2, [3, [4, [5, [6]]]]]], [7, 8]]),
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
        )
        self.assertEqual(flatter(["f", ["l", ["a", ["t", ["t", ["e", ["r"]]]]]]]), ["f","l","a","t","t","e","r"])

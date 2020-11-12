import unittest


class Vector2D:
    # Maintain two pointers, row and col, that points to the next item to return.
    def __init__(self, v):
        self.v = v
        self.row = -1
        self.go_to_next_nonempty_row()
        self.col = 0

    def next(self) -> int:
        ret = self.v[self.row][self.col]
        self.col += 1
        if self.col == len(self.v[self.row]):
            self.go_to_next_nonempty_row()
            self.col = 0
        return ret

    def hasNext(self) -> bool:
        return self.row  < len(self.v) and self.col < len(self.v[self.row])

    def go_to_next_nonempty_row(self):
        self.row += 1
        while self.row < len(self.v) and len(self.v[self.row]) == 0:
            self.row += 1


class TestFlatten(unittest.TestCase):
    def test_input1(self):
        my_list = [[1, 3, 4], [5], [2, 3]]
        my_vector = Vector2D(my_list)
        self.assertTrue(my_vector.hasNext())
        self.assertEqual(my_vector.next(), 1)
        self.assertEqual(my_vector.next(), 3)
        self.assertEqual(my_vector.next(), 4)
        self.assertTrue(my_vector.hasNext())
        self.assertEqual(my_vector.next(), 5)
        self.assertTrue(my_vector.hasNext())
        self.assertEqual(my_vector.next(), 2)
        self.assertEqual(my_vector.next(), 3)
        self.assertFalse(my_vector.hasNext())


if __name__ == '__main__':
    unittest.main()
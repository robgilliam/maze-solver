import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        for num_cols, num_rows in [(12, 10), (2, 3), (8, 8)]:
            with self.subTest(num_cols = num_cols, num_rows = num_rows):
                m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
                self.assertEqual(
                    len(m1._cells),
                    num_cols,
                )
                self.assertEqual(
                    len(m1._cells[0]),
                    num_rows,
                )

if __name__ == "__main__":
    unittest.main()

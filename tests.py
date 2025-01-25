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

    def test_break_entrance_and_exit(self):
        for num_cols, num_rows in [(12, 10), (2, 3), (8, 8)]:
            with self.subTest(num_cols = num_cols, num_rows = num_rows):
				# Arrange
                m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

                # Assume
                self.assertTrue(m1._cells[0][0].has_top_wall)
                self.assertTrue(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

				# Act
                m1._break_entrance_and_exit()

				# Assert
                self.assertFalse(m1._cells[0][0].has_top_wall)
                self.assertFalse(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

if __name__ == "__main__":
    unittest.main()

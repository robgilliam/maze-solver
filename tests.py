import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        for num_cols, num_rows in [(12, 10), (2, 3), (8, 8)]:
            with self.subTest(num_cols = num_cols, num_rows = num_rows):
                m = Maze(0, 0, num_rows, num_cols, 10, 10)
                self.assertEqual(
                    len(m._cells),
                    num_cols,
                )
                self.assertEqual(
                    len(m._cells[0]),
                    num_rows,
                )

    def test_break_entrance_and_exit(self):
        for num_cols, num_rows in [(12, 10), (2, 3), (8, 8)]:
            with self.subTest(num_cols = num_cols, num_rows = num_rows):
				# Arrange
                m = Maze(0, 0, num_rows, num_cols, 10, 10)

                # Assume
                self.assertTrue(m._cells[0][0].has_top_wall)
                self.assertTrue(m._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

				# Act
                m._break_entrance_and_exit()

				# Assert
                self.assertFalse(m._cells[0][0].has_top_wall)
                self.assertFalse(m._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

    def test_reset_cells_visited(self):
        # Arrange
        m = Maze(0, 0, 10, 10, 10, 10)
        for col in m._cells:
            for cell in col:
                cell.visited = True

        # Assume
        for col in m._cells:
            for cell in col:
                self.assertTrue(cell.visited)

        # Act
        m._reset_cells_visited()

        # Assert
        for col in m._cells:
            for cell in col:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()

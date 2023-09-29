from solver import full_grid, new_partial_grid
import time
import unittest

class TestSolverMethods(unittest.TestCase):

    def test_solver(self):
        expected = full_grid()
        actual = new_partial_grid(31, expected)
        full_grid(actual)
        self.assertEqual(sorted(expected), sorted(actual))

if __name__ == '__main__':
    unittest.main()

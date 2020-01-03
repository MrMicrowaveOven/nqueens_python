import sys
sys.path.append("../lib")

import unittest

from board import Board
from space import Space

class BoardTest(unittest.TestCase):
    def test_board_init(self):
        b = Board(4, [[1,2],[3,0]])
        assert b.queen_in_row(0) == None
        assert b.queen_in_row(1) == 2
        assert b.queen_in_row(2) == None
        assert b.queen_in_row(3) == 0

    def test_place_queen(self):
        b = Board(2)
        b.place_queen([0,1])
        self.assertEquals(b.queen_in_row(0), 1)
        self.assertEquals(b.queen_in_row(1), None)
        # assert b.spaces == board_with_queen, "board doesn't have queen in correct spot"

    def test_queen_in_row(self):
        b = Board(4)
        b.place_queen([1,2])
        self.assertEquals(b.queen_in_row(1), 2)

    def test_horizontal_captures(self):
        b = Board(4)
        queen_space = [3,1]
        horizontal_captures = [[3,0],[3,2],[3,3]]
        self.assertEquals(b.horizontal_captures(queen_space), horizontal_captures)

    def test_vertical_captures(self):
        b = Board(4)
        queen_space = [1,2]
        vertical_captures = [[0,2],[2,2],[3,2]]
        self.assertEquals(b.vertical_captures(queen_space), vertical_captures)

    def test_vertical_captures_2(self):
        b = Board(5)
        queen_space = [3,1]
        diagonal_captures = [
            [2,0],
            [2,2], [1,3], [0,4],
            [4,0],
            [4,2]
        ]
        self.assertEquals(b.diagonal_captures(queen_space), diagonal_captures)

    def test_diagonal_captures(self):
        b = Board(4)
        queen_space = [1,2]
        diagonal_captures = [[0,1], [0,3], [2,1], [3, 0], [2, 3]]
        diagonal_captures.sort()

        calculated_diagonal_captures = b.diagonal_captures(queen_space)
        calculated_diagonal_captures.sort()

        self.assertEquals(calculated_diagonal_captures, diagonal_captures)

    def test_get_captures(self):
        b = Board(4)
        queen_space = [1,1]
        captures = [
            [1,0],[1,2],[1,3],
            [0,1],[2,1],[3,1],
            [0,0],[0,2],[2,0],[2,2],[3,3]
        ]

        self.assertEquals(captures, b.get_captures(queen_space))

    def test_get_queens(self):
        b = Board(4)
        queen_spaces = [[0,0],[1,2],[2,0],[3,3]]
        for queen_space in queen_spaces:
            b.place_queen(queen_space)
        self.assertEquals(b.get_queens(), queen_spaces)

if __name__ == "__main__":
    unittest.main()

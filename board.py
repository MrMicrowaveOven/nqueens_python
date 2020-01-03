from space import Space
class Board:
    def __init__(self, size, prefill = []):
        self.size = size
        spaces = [0] * size
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Space())
            spaces[i] = row
        self.spaces = spaces
        for spot in prefill:
            self.place_queen(spot)

    def show_board(self):
        spaces = self.spaces
        board_array = []
        for row in spaces:
            row_array = []
            for space in row:
                if space.is_filled():
                    row_array.append(1)
                else:
                    row_array.append(0)
            board_array.append(row_array)
        for row_array in board_array:
            print row_array

    def place_queen(self, spot):
        spaces = self.spaces
        space = spaces[spot[0]][spot[1]]
        space.fill()

    def get_queens(self):
        size = self.size
        queens = []
        for i in range(size):
            queens.append([i,self.queen_in_row(i)])
        return queens

    def is_solution(self):
        queens = self.get_queens()
        for queen in queens:
            captures = self.get_captures(queen)
            other_queens = queens
            other_queens.remove(queen)
            # Intersection of captures and other_queens
            collisions = [spot for spot in other_queens if spot in captures]
            if len(collisions) > 0:
                return False
        return True

    def queen_in_row(self, row_index):
        spaces = self.spaces
        row = spaces[row_index]

        for space_index in range(len(row)):
            space = row[space_index]
            if space.is_filled():
                return space_index
        return None

    def get_captures(self ,space):
        return self.horizontal_captures(space) + self.vertical_captures(space) + self.diagonal_captures(space)

    def horizontal_captures(self, space):
        size = self.size
        space_row = space[0]
        horizontal_spaces = []
        for i in range(size):
            if i != space[1]:
                horizontal_spaces.append([space_row, i])
        return horizontal_spaces

    def vertical_captures(self, space):
        size = self.size
        space_column = space[1]
        vertical_spaces = []
        for i in range(size):
            if i != space[0]:
                vertical_spaces.append([i, space_column])
        return vertical_spaces

    def diagonal_captures(self, space):
        size = self.size
        diagonals = []
        # Up-Left
        space_dup = space
        while space_dup[0] >= 0 and space_dup[1] >= 0:
            space_dup = space_dup[:]
            space_dup[0] -= 1
            space_dup[1] -= 1
            if space_dup[0] >= 0 and space_dup[1] >= 0:
                diagonals.append(space_dup)
        # Up-Right
        space_dup = space
        while space_dup[0] >= 0 and space_dup[1] < size:
            space_dup = space_dup[:]
            space_dup[0] -= 1
            space_dup[1] += 1
            if space_dup[0] >= 0 and space_dup[1] < size:
                diagonals.append(space_dup)
        # Down-Left
        space_dup = space
        while space_dup[0] < size and space_dup[1] >= 0:
            space_dup = space_dup[:]
            space_dup[0] += 1
            space_dup[1] -= 1
            if space_dup[0] < size and space_dup[1] >= 0:
                diagonals.append(space_dup)
        # Down-Right
        space_dup = space
        while space_dup[0] < size and space_dup[1] < size:
            space_dup = space_dup[:]
            space_dup[0] += 1
            space_dup[1] += 1
            if space_dup[0] < size and space_dup[1] < size:
                diagonals.append(space_dup)
        return diagonals

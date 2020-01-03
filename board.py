from space import Space
class Board:
    def __init__(self, size):
        self.size = size
        spaces = [0] * size
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Space())
            spaces[i] = row
        self.spaces = spaces

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

    def queen_in_row(self, row_index):
        spaces = self.spaces
        row = spaces[row_index]

        for space_index in range(len(row)):
            space = row[space_index]
            if space.is_filled():
                return space_index
        return None

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

from board import Board

b = Board(4)

b.show_board()

b.place_queen([1,3])
print '-------------------------'
b.show_board()

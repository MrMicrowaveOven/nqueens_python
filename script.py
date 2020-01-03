from board import Board

b = Board(4)

queens = [
    [0,0],
    [1,2],
    [2,1],
    [3,3]
]

for queen in queens:
    b.place_queen(queen)

b.show_board()
print b.is_solution()

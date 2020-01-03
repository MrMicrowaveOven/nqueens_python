from board import Board

import random

def find_solution(size):
    random_board = make_random_board(size)
    b = Board(size, random_board)
    while not b.is_solution():
        random_board = make_random_board(size)
        b = Board(size, random_board)
    print 'solution found!'
    b.show_board()

def make_random_board(size):
    queens = []
    row_indices = range(size)
    scrambled = range(size)
    random.shuffle(scrambled)
    for i in row_indices:
        queens.append([row_indices[i],scrambled[i]])
    return queens

from datetime import datetime
print datetime.now()
find_solution(10)
print datetime.now()

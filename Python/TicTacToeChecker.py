from itertools import chain


def is_solved(board):
    one_dim_board = list(chain(*board))
    possible_solutions = [
        (0, 1, 2), (3, 4, 5),
        (6, 7, 8), (0, 3, 6),
        (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for i, j, k in possible_solutions:
        if one_dim_board[i] == one_dim_board[j] == one_dim_board[k] != 0:
            return one_dim_board[i]

    if 0 in one_dim_board:
        return -1
    return 0


if __name__ == '__main__':
    board = [[0, 0, 2],
             [0, 0, 0],
             [1, 0, 1]]

    print(is_solved(board))

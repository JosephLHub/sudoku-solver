example_board = [
    0, 0, 1, 3, 9, 2, 0, 0, 0,
    0, 0, 3, 0, 0, 7, 0, 4, 5,
    0, 0, 7, 0, 0, 0, 0, 0, 9,
    0, 0, 6, 5, 0, 0, 0, 7, 0,
    2, 0, 0, 0, 0, 0, 0, 0, 1,
    0, 9, 0, 0, 0, 1, 4, 0, 0,
    5, 0, 0, 0, 0, 0, 9, 0, 0,
    6, 1, 0, 2, 0, 0, 8, 0, 0,
    0, 0, 0, 9, 0, 8, 5, 0, 0,
]

def get_subsquares(board):
    subsquares, first, second, third = [], [], [], []
    for tile in range(len(board)):
        if tile % 9 < 3:
            first.append(board[tile])
        elif 2 < tile % 9 < 6:
            second.append(board[tile])
        else:
            third.append(board[tile])
        if tile % 27 == 26:
            subsquares.append(first)
            subsquares.append(second)
            subsquares.append(third)
            first, second, third = [], [], []
    return subsquares

for tile in range(len(example_board)): #Convert all 0s to lists of possible numbers
    if example_board[tile] == 0:
        example_board[tile] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

solved = False

def check_solved(board): #Check if every tile only has 1 possible number
    return all([isinstance(tile, int) for tile in board])

def axes_prune(board): #add column checks
    for row in range(9):
        for tile in range(9):
            nums = [x for x in board[row * 9 : (row * 9) + 9] if isinstance(x, int)]
            for num in nums:
                if not isinstance(board[(row * 9) + tile], int):
                    board[(row * 9) + tile].remove(num)
    return board

def subsquares_prune(board):
    for square in range(9):
        square_nums
    return board

board = subsquares_prune([])

while not solved:
    solved = check_solved(example_board)
    pass

squares = get_subsquares(example_board)
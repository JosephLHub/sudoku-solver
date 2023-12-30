example_board = [
    0, 5, 1, 3, 9, 2, 0, 0, 0,
    9, 2, 3, 0, 0, 7, 0, 4, 5,
    8, 6, 7, 0, 0, 0, 0, 0, 9,
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

def axes_prune(board): #add column checks
    for row in range(9):
        nums = [x for x in board[row * 9 : (row * 9) + 9] if isinstance(x, int)]
        for tile in range(9):
            if not isinstance(board[(row * 9) + tile], int):
                board[(row * 9) + tile] = [num for num in board[(row * 9) + tile] if num not in nums] #Remove all other numbers in row from possibilities
    for col in range(9):
        nums = []
        for x in range(9):
            if isinstance(board[(x * 9) + col], int):
                nums.append(board[(x * 9) + col])
        for tile in range(9):
            if not isinstance(board[(tile * 9) + col], int):
                board[(tile * 9) + col] = [num for num in board[(tile * 9) + col] if num not in nums]
    return board

def subsquares_prune(board): #Remove solved numbers from possibilities in each 3x3 square
    subsquares = get_subsquares(board)
    for square in range(9):
        nums = [x for x in subsquares[square] if isinstance(x, int)] #Get all solved numbers in subsquare
        for tile in range(9):
            curr_tile = ((square % 3) * 3) + (27 * (square // 3)) + ((tile % 3)) + (9 * (tile // 3)) #Match subsquare tile to normal board tile
            if not isinstance(board[curr_tile], int):
                board[curr_tile] = [num for num in board[curr_tile] if num not in nums] #Remove all other numbers in subsquare from possibilities
    return board

def format_board(board): #Convert 1-long tile possibilities to solved numbers
    for tile in range(len(board)):
        if not isinstance(board[tile], int) and len(board[tile]) == 1:
            board[tile] = board[tile][0]
    return board

def check_solved(board): #Check if every tile only has 1 possible number
    return all([isinstance(tile, int) for tile in board])

board = example_board
solved = False
i = 0
while not solved:
    board = axes_prune(board)
    board = format_board(board)
    board = subsquares_prune(board)
    board = format_board(board)
    solved = check_solved(board)
    i += 1
    if i > 999:
        solved = True

print(board[0:9])
print(board[9:18])
print(board[18:27])
print(board[27:36])
print(board[36:45])
print(board[45:54])
print(board[54:63])
print(board[63:72])
print(board[72:81])
import heapq

EMPTY = 0

def print_board(board):
    for row in board:
        print(row)

def is_valid(board, row, col, num):

    if num in board[row]:
        return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def get_next_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == EMPTY:
                return i, j
    return None

def heuristic(board):
    empty_cell = get_next_empty_cell(board)
    if empty_cell is None:
        return 0
    else:
        return 1

def astar(board):
            
    open_list = [(heuristic(board), board)]
    print(open_list)
    closed_list = set()

    while open_list:

        current_score, current_board = heapq.heappop(open_list)
        closed_list.add(tuple(map(tuple, current_board)))

        empty_cell = get_next_empty_cell(current_board)
        if empty_cell is None:
            return current_board

        row, col = empty_cell
        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                new_board = [row.copy() for row in current_board]
                new_board[row][col] = num
                if tuple(map(tuple, new_board)) not in closed_list:
                    heapq.heappush(open_list, (heuristic(new_board), new_board))

    return None


def play_game():
    board = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print("Welcome to Sudoku!")
    print_board(board)

    solution = astar(board)
    if solution:
        print("Solution:")
        print_board(solution)
    else:
        print("No solution found.")


play_game()
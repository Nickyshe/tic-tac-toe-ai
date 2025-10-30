
def play(board):
    x_count = board.count('x')
    o_count = board.count('o')

    if x_count == o_count:
        current_player = 'x'  # Equal counts → X's turn
    else:
        current_player = 'o'  # X has more → O's turn

    if current_player == 'x':
        opponent = 'o'
    else:
        opponent = 'x'


    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]

    def can_win_on_line(player):
        for line in winning_lines:
            line_state = [board[pos] for pos in line]
            if line_state.count(player) == 2 and line_state.count('') == 1:
                for pos in line:
                    if board[pos] == '':
                        return pos
                return None

                # Priority 1: Can I win?
        win_move = can_win_on_line(current_player)
        if win_move is not None:
            return win_move

        # Priority 2: Must I block?
        block_move = can_win_on_line(opponent)
        if block_move is not None:
            return block_move

                # Priority 3: Take center
        if board[4] == '':
            return 4

                # Priority 4: Take a corner
        for corner in [0, 2, 6, 8]:
            if board[corner] == '':
                return corner

                # Priority 5: Take a side
        for side in [1, 3, 5, 7]:
            if board[side] == '':
                return side

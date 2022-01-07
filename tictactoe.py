def init_game():
    game_state = dict()  # keys --> (i, j), where i is the row and j is the column
    return game_state


def print_game_state(game_state):
    board_str = ""
    for i in range(3):
        for j in range(3):
            entry = game_state[(i, j)] if (i, j) in game_state.keys() else "  "
            if j != 2:
                board_str += f"{entry} | "
            else:
                board_str += f"{entry}\n"
                if i != 2:
                    board_str += "------------\n"
    return board_str


# Player is either X or O
# pos is (i, j), where i is the row of the board, j is the column
def take_turn(game_state, player, pos):
    if pos[0] < 0 or pos[0] > 2 or pos[1] < 0 or pos[1] > 2:
        print("POSITION IS OUT OF RANGE")
        return player
    if pos in game_state.keys():
        print("POSITION ALREADY TAKEN")
        return player
    game_state[pos] = player
    return "O" if player == "X" else "X"


def check_win(game_state):
    for i in range(3):  # Check rows
        if (i, 0) in game_state.keys() and (i, 1) in game_state.keys() and (i, 2) in game_state.keys():
            row = game_state[(i, 0)] + game_state[(i, 1)] + game_state[(i, 2)]
            if row == "OOO":
                return "O"
            elif row == "XXX":
                return "X"
    for j in range(3):  # Check columns
        if (0, j) in game_state.keys() and (1, j) in game_state.keys() and (2, j) in game_state.keys():
            col = game_state[(0, j)] + game_state[(1, j)] + game_state[(2, j)]
            if col == "OOO":
                return "O"
            elif col == "XXX":
                return "X"
    if (0, 0) in game_state.keys() and (1, 1) in game_state.keys() and (2, 2) in game_state.keys():
        down_diag = game_state[(0, 0)] + game_state[(1, 1)] + game_state[(2, 2)]
        if down_diag == "OOO":
            return "O"
        elif down_diag == "XXX":
            return "X"
    if (2, 0) in game_state.keys() and (1, 1) in game_state.keys() and (0, 2) in game_state.keys():
        up_diag = game_state[(2, 0)] + game_state[(1, 1)] + game_state[(0, 2)]
        if up_diag == "OOO":
            return "O"
        elif up_diag == "XXX":
            return "X"
    return None

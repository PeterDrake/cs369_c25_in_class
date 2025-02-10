INITIAL_STATE = '.........'

def successor(state, index, player):
    return state[:index] + player + state[index+1:]

def legal_moves(state):
    return [i for i in range(len(state)) if state[i] == '.']

def winner(state):
    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]
    for line in lines:
        if state[line[0]] == state[line[1]] == state[line[2]]:
            player = state[line[0]]
            if player == 'X':
                return 1
            if player == 'O':
                return -1
    return 0


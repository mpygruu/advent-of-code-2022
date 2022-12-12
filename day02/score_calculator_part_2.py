SHAPE_TO_PLAY = {
    'A Y': 'rock',
    'B Z': 'scissors',
    'C X': 'paper',
    'A X': 'scissors',
    'B Y': 'paper',
    'C Z': 'rock',
    'A Z': 'paper',
    'B X': 'rock',
    'C Y': 'scissors'
}


def calculate_score(game_data):
    score = 0

    for round in game_data:
        score += __shape_score(round)
        score += __result_score(round[2])  

    return score


def __shape_score(round):
    if SHAPE_TO_PLAY[round] == 'rock':
        return 1
    elif SHAPE_TO_PLAY[round] == 'paper':
        return 2
    elif SHAPE_TO_PLAY[round] == 'scissors':
        return 3

    return 0


def __result_score(round_move):
    if round_move == 'Z':
        return 6
    elif round_move == 'Y':
        return 3
    
    return 0
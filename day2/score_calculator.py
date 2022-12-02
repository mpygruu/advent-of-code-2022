ROUND_RESULT = {
    'A Y': 'win',
    'B Z': 'win',
    'C X': 'win',
    'A X': 'draw',
    'B Y': 'draw',
    'C Z': 'draw',
    'A Z': 'lose',
    'B X': 'lose',
    'C Y': 'lose'
}

def calculate_score(game_data):
    score = 0

    for round in game_data:
        score += __shape_score(round[2])
        score += __result_score(round)  

    return score


def __shape_score(shape):
    if shape == 'X':
        return 1
    elif shape == 'Y':
        return 2
    elif shape == 'Z':
        return 3

    return 0


def __result_score(round):
    result = ROUND_RESULT[round]

    if  result == 'win':
        return 6
    elif result == 'draw':
        return 3
    
    return 0
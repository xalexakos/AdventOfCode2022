PROBLEM_1_POINTS = {
    ###
    # A = R = X  1
    # B = P = Y  2
    # C = S = Z  3
    # R > S - S > P - P > R
    ###
    'A X': 1 + 3,
    'A Y': 2 + 6,
    'A Z': 3 + 0,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 1 + 6,
    'C Y': 2 + 0,
    'C Z': 3 + 3
}

PROBLEM_2_POINTS = {
    ###
    # X LOSE
    # Y DRAW
    # Z WIN
    ###
    'A X': 3 + 0,
    'A Y': 1 + 3,
    'A Z': 2 + 6,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 2 + 0,
    'C Y': 3 + 3,
    'C Z': 1 + 6
}


def calculate_solution(input_data, points):
    score = 0

    playlist = [d for d in input_data]
    for m in playlist:
        score += points[m]

    return score

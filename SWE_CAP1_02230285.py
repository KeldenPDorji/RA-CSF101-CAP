################################
# Kelden Phuntsho Dorji
# Section A
# 02230285
################################

# REFERENCES
# Links that you referred while solving the problem
# https://learningpenguin.net/2020/02/06/a-simple-algorithm-for-calculating-the-result-of-rock-paper-scissors-game/# 
# https://stackoverflow.com/questions/13126510/python-rock-paper-scissors-score-counter
# https://athena.ecs.csus.edu/~buckley/CSc191/RockPaperScissors.pdf

# SOLUTION
# Your Solution Score:
# 63404
################################

# Define mappings for moves and scoring system
moves = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
score_mapping = {'rock': 1, 'paper': 2, 'scissors': 3}
outcome_scores = {'lose': 0, 'draw': 3, 'win': 6}

# Function to determine the move for a draw
def draw(opponent_move):
    return opponent_move

# Function to determine the move for a loss
def lose(opponent_move):
    return 'rock' if opponent_move == 'scissors' else 'scissors' if opponent_move == 'paper' else 'paper'

# Function to determine the move for a win
def win(opponent_move):
    return 'scissors' if opponent_move == 'rock' else 'rock' if opponent_move == 'scissors' else 'paper'

# Function to calculate the score for a single round
def calculate_round_score(opponent_move, desired_outcome):
    opponent_move_value = moves[opponent_move]
    if desired_outcome == 'Y':
        correct_move = draw(opponent_move_value)
    elif desired_outcome == 'X':
        correct_move = lose(opponent_move_value)
    else:
        correct_move = win(opponent_move_value)
    score = score_mapping[correct_move]
    if correct_move == opponent_move_value:
        score += outcome_scores['win']
    elif correct_move != opponent_move_value:
        score += outcome_scores['draw']
    return score

# Function to calculate the total score by processing a file with game records
def calculate_total_score(filename):
    total_score = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        opponent_move, desired_outcome = line.strip().split()
        round_score = calculate_round_score(opponent_move, desired_outcome)
        total_score += round_score
    return total_score

# Function to read the input file and display the total score
def read_input():
    filename = 'input_5_cap1.txt'
    total_score = calculate_total_score(filename)
    print(f"The total score is: {total_score}")

# Start the program by reading the input file
read_input()

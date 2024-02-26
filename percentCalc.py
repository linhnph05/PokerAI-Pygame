import CalcFunction

def run_simulation(hole_cards, given_board, deck, exact = False, num = 10000):
    num_players = len(hole_cards)

    result_histograms, winner_list = [], [0] * (num_players + 1)
    for _ in range(num_players):
        result_histograms.append([0] * len(CalcFunction.hand_rankings))

    board_length = 0 if given_board is None else len(given_board)

    if exact or given_board is not None:
        generate_boards = CalcFunction.generate_exhaustive_boards
    else:
        generate_boards = CalcFunction.generate_random_boards
        
    CalcFunction.find_winner(generate_boards, deck, hole_cards, num,
                                 board_length, given_board, winner_list,
                                 result_histograms)
    return CalcFunction.find_winning_percentage(winner_list)

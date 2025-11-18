import random
#test
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card"""
    global cards
    return random.choice(cards)


def clear_screen():
    """Artificially clearing the screen by using line spacing (since clearing screen aren't supported by IDE console)"""
    print("\n" * 20)


def calculate_score(cards):
    """Calculate the score of a blackjack hand"""
    if sum(cards) == 21 and len(cards) == 2:
        return -1

    while 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1

    return sum(cards)

def check_win(player_score, computer_score):
    if player_score == computer_score:
        return "It's a Draw."
    elif computer_score == -1:
        return "You lose, opponent has Blackjack."
    elif player_score == -1:
        return "You win, You got a Blackjack."
    elif player_score > 21:
        return "You lose, you went over."
    elif computer_score > 21:
        return "You win, opponent went over. "
    elif player_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    """Start the blackjack game"""
    player_cards = []
    computer_cards = []
    player_score = 0
    computer_score = 0
    is_game_over = False

    # Initial Deal
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == -1 or  computer_score == -1 or player_score > 21:
            is_game_over = True
        else:
            if input("Type 'h' to hit, type 's' to stand: ").lower() == 'h':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    #Computer hit or stand
    while computer_score != -1 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(check_win(player_score, computer_score))


if __name__ == '__main__':
    while input("Ready to play a game of Blackjack ? Type 'y' or 'n': ").lower() == 'y':
        clear_screen()
        play_game()

    print('Thanks for Playing!, Goodbye!')




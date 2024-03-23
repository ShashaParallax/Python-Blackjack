import random
from art import logo


def card_deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def score_comparison(player, computer):
    if (sum(player) > sum(computer)) and (sum(player) > 21):
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer}, final score {sum(computer)}")
        print("You went over, You lose.")
    elif sum(player) > sum(computer):
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer}, final score {sum(computer)}")
        print("You Win!")
    elif (sum(player) < sum(computer)) and (sum(computer) > 21):
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer}, final score {sum(computer)}")
        print("Opponent went over, You Win!")
    elif sum(player) < sum(computer):
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer}, final score {sum(computer)}")
        print("You Lose.")
    else:
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer}, final score {sum(computer)}")
        print("It's a draw.")


print(logo)


def game():
    player_cards = []
    computer_cards = []
    while len(player_cards) < 2:
        player_cards.append(card_deal())
        computer_cards.append(card_deal())

    revealed_card = computer_cards[0]
    print(f"Your cards: {player_cards}")
    if revealed_card == 11:
        revealed_card = computer_cards[1]
    print(f"Computer's first card: {revealed_card}")

    should_player_draw = True
    while should_player_draw:
        should_continue = input("Type 'y' to draw another card, type 'n' to pass: ")
        if should_continue == "y":
            player_cards.append(card_deal())
            if sum(player_cards) > 21:
                score_comparison(player_cards, computer_cards)
                should_player_draw = False
            else:
                print(f"Your current hand: {player_cards}")
        else:
            if 11 in player_cards and (sum(player_cards) > 21):
                player_cards[player_cards.index(11)] = 1
            if 11 in computer_cards and (sum(computer_cards) > 21):
                computer_cards[computer_cards.index(11)] = 1
            while sum(computer_cards) < 17:
                computer_cards.append(card_deal())
            score_comparison(player_cards, computer_cards)
            should_player_draw = False

    if (input("Type 'y' to play again, type 'n' to stop: ")) == "y":
        game()


game()

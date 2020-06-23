import Deck


def calculate_sum(hand):
    total = 0
    ace_count = 0
    for i in hand:
        if i == 1:
            total += 11
            ace_count += 1
        elif i == 12 or i == 13:
            total += 11
        else:
            total += i
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total


def dealer_turn(game_deck, player, dealer, player_sum, dealer_sum):
    while True:
        dealer.append(game_deck.take_card())
        dealer_sum = calculate_sum(dealer)
        display(player, dealer, player_sum, dealer_sum)
        if player_sum < dealer_sum < 22:
            print("You've lost! Dealer has a higher sum than you.")
            return
        elif dealer_sum > 21:
            print("Dealer busted! You've won!")
            return


def display(player, dealer, player_sum, dealer_sum):
    print_list = []
    print("Your Cards: ")
    for card in player:
        if card == 1:
            print_list.append("Ace")
        elif card == 11:
            print_list.append("Jack")
        elif card == 12:
            print_list.append("Queen")
        elif card == 13:
            print_list.append("King")
        else:
            print_list.append(card)
    print(print_list)
    print("Your current sum:")
    print(player_sum)

    print()

    print_list2 = []
    hidden_card = 0
    print("Dealer Cards:")
    for index, card in enumerate(dealer):
        if index == 1:
            print_list2.append("?")
            hidden_card = card
            continue
        elif card == 1:
            print_list2.append("Ace")
        elif card == 11:
            print_list2.append("Jack")
        elif card == 12:
            print_list2.append("Queen")
        elif card == 13:
            print_list2.append("King")
        else:
            print_list2.append(card)
    print(print_list2)

    print("Dealer current sum:")
    print(dealer_sum - hidden_card)

    print()

def initialize():
    game_deck = Deck.Deck()
    game_deck.create_deck()
    player = []
    dealer = []

    # give both players two cards
    player.append(game_deck.take_card())
    player.append(game_deck.take_card())
    dealer.append(game_deck.take_card())
    dealer.append(game_deck.take_card())

    player_sum = calculate_sum(player)
    dealer_sum = calculate_sum(dealer)

    display(player, dealer, player_sum, dealer_sum)

    return game_deck, player, dealer, player_sum, dealer_sum


def run_game():
    print("Welcome to Blackjack")

    game_deck, player, dealer, player_sum, dealer_sum = initialize()

    while True:
        choice = input("Player, would you like to: \n     1. Hit\n     2. Stay\n")

        if choice == '1':
            player.append(game_deck.take_card())
            player_sum = calculate_sum(player)
            display(player, dealer, player_sum, dealer_sum)
            if player_sum > 21:
                print("You busted!")
                return
        elif choice == '2':
            print("Okay, time for the dealer to go.")
            dealer_turn(game_deck, player, dealer, player_sum, dealer_sum)
            break
        else:
            print("Invalid Choice, please enter 1 or 2.")
            continue


if __name__ == '__main__':
    run_game()

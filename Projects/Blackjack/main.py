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
        if player_sum < dealer_sum < 22:
            display(player, dealer, player_sum, dealer_sum, True)
            print("You've lost! Dealer has a higher sum than you.")
            return
        elif dealer_sum > 21:
            display(player, dealer, player_sum, dealer_sum, True)
            print("Dealer busted! You've won!")
            return
        display(player, dealer, player_sum, dealer_sum, False)


def display(player, dealer, player_sum, dealer_sum, win_flag):
    # print player cards and sum
    print_list_player = []
    print("Your Cards: ")
    for card in player:
        if card == 1:
            print_list_player.append("Ace")
        elif card == 11:
            print_list_player.append("Jack")
        elif card == 12:
            print_list_player.append("Queen")
        elif card == 13:
            print_list_player.append("King")
        else:
            print_list_player.append(card)
    print(*print_list_player, sep=', ')
    print("Your current sum:")
    print(player_sum)

    print()

    # print dealer cards and sum
    print_list2 = []
    hidden_card = 0
    print("Dealer Cards:")
    for index, card in enumerate(dealer):
        if index == 1 and not win_flag:
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
    print(*print_list2, sep=', ')

    print("Dealer current sum:")
    if win_flag:
        print(dealer_sum)
    else:
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

    display(player, dealer, player_sum, dealer_sum, False)

    return game_deck, player, dealer, player_sum, dealer_sum


def run_game():
    print("Welcome to Blackjack")

    game_deck, player, dealer, player_sum, dealer_sum = initialize()

    while True:
        choice = input("Player, would you like to: \n     1. Hit\n     2. Stay\n")

        if choice == '1':
            player.append(game_deck.take_card())
            player_sum = calculate_sum(player)
            if player_sum > 21:
                display(player, dealer, player_sum, dealer_sum, True)
                print("You busted!")
                return
            else:
                display(player, dealer, player_sum, dealer_sum, False)
        elif choice == '2':
            print("Okay, time for the dealer to go.\n")
            dealer_turn(game_deck, player, dealer, player_sum, dealer_sum)
            break
        else:
            print("Invalid Choice, please enter 1 or 2.")
            continue


if __name__ == '__main__':
    run_game()
    while True:
        play_again = input("Would you like to play again? Y/N\n")
        if play_again == 'Y':
            run_game()
        elif play_again == 'N':
            print("Goodbye!")
            break
        else:
            print("Invalid input")



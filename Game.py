#############################################################################
# # Game Rules
# Player needs to get as close to 21 as much as possible without going over
# Dealer hits until it reaches 17
# Aces count as 1 or 11
# At the start of game the player hwill ave 100 Chips
###############################################################################

import random
from Card import Card
from Deck import Deck
from Hand import Hand
from Error import Error
from Chips import Chips

## Game Logic
if __name__ == "__main__":

    total_chips = Chips()
    print("Welcome to the BlackJack Game")

    while True:
        print("How many chips would you like to bet? (1-100):")
        
        # Check if the chips count enetered is an integer valules and enough count to play
        chip_count = Error().chip_error(total_chips.total)
        player = Hand()
        dealer = Hand()
        card_in_game = Deck(Card().all_card)

        # Use random function to generate cards for the player and dealers
        # First card for the dealer
        random_choice = random.choices(card_in_game.cards)
        # Pop by index for the card in game
        card_in_game.Deck_pop(card_in_game.find_idx(random_choice[0]))
        dealer.add_card(random_choice, card_in_game.cart[random_choice[0][0]])
        #  second card for the dealer
        random_choice = random.choices(card_in_game.cards)
        card_in_game.Deck_pop(card_in_game.find_idx(random_choice[0]))
        dealer.add_card(random_choice, card_in_game.cart[random_choice[0][0]])
        print("-------------------------------------------------------------------------------------------")
        print("Dealer has cards: <<Card1 Hidden>> ", dealer.Card_in_hand[1][0])
        print("-------------------------------------------------------------------------------------------")
        
        #  Generate 2 cards for player using random function
        random_choice = random.choices(card_in_game.cards)

        card_in_game.Deck_pop(
            card_in_game.find_idx(random_choice[0])
        )  
        player.add_card(
            random_choice, card_in_game.cart[random_choice[0][0]]
        )  
        random_choice = random.choices(card_in_game.cards)

        card_in_game.Deck_pop(card_in_game.find_idx(random_choice[0]))

        player.add_card(random_choice, card_in_game.cart[random_choice[0][0]])
        
        # Display the player cards
        print("-------------------------------------------------------------------------------------------")
        print("Player has cards:", player.Card_in_hand[0][0], ",", player.Card_in_hand[1][0] ,"\n", " Total ", player.value)
        print("-------------------------------------------------------------------------------------------")
        
        # Loop for the game conditions(win/loose/cotinue)
        loop_val = player.hand_win()

        # Check conditions for the player
        while True:
            if player.hand_win() == "Win":
                print("player Win")
                loop_val = player.hand_win()
                total_chips.add(chip_count)
                break

            elif player.hand_win() == "Loose":
                print("player Looses..... Better Luck next time")
                loop_val = player.hand_win()
                total_chips.remove(chip_count)
                break
            else:
                print("Do you want a hit? (Y/N): ")
                hit_status = Error().in_Error()  
                if hit_status == "y" or hit_status == "Y":
                    random_choice = random.choices(
                        card_in_game.cards
                    )  
                    card_in_game.Deck_pop(
                        card_in_game.find_idx(random_choice[0])
                    )  
                    # Add card to the player list
                    player.add_card(
                        random_choice, card_in_game.cart[random_choice[0][0]]
                    )
                    # Display the player cards after hit condition
                    print("-------------------------------------------------------------------------------------------")
                    print( "Player cards after hit are: ", [[number for number in group] for group in player.Card_in_hand], "\n", "Total: ", player.value)
                    print("-------------------------------------------------------------------------------------------")
                    
                else:
                    print("-------------------------------------------------------------------------------------------")
                    print("Dealer cards are: <<Card1 Hidden>> ", player.Card_in_hand[1][0], "\n", " Total ", dealer.value)
                    print("-------------------------------------------------------------------------------------------")
                    loop_val = player.hand_win()
                    break

        # Dealer turn
        while loop_val == "Go on":  

            if dealer.hand_win() == "Win":
                print("Dealer Win")
                total_chips.remove(chip_count)
                break

            elif dealer.hand_win() == "Loose":
                print("Dealer Looses")
                total_chips.add(chip_count)
                break

            elif dealer.value < 17:  # 17 > dealer  , dealer +1 card
                # Add card for the dealer
                random_choice = random.choices(
                    card_in_game.cards)
                         
                card_in_game.Deck_pop(
                    card_in_game.find_idx(random_choice[0])
                )  
                dealer.add_card(
                    random_choice, card_in_game.cart[random_choice[0][0]]
                )  
                print("-------------------------------------------------------------------------------------------")
                print( "Dealer cards after hit are: ", [[number for number in group] for group in dealer.Card_in_hand], "\n", "Total: ", dealer.value)
                print("-------------------------------------------------------------------------------------------")

            elif (
                dealer.value >= 17 and dealer.value > player.value
            ):  #    
                print("Dealer Win")
                total_chips.remove(chip_count)
                break
            else:  
                print("Player Win")
                total_chips.add(chip_count)
                break

        if total_chips.total == 0:
            print("Sorry, you have 0 Chips.", "\n", "Game over!!!!")
            break

        print("Do you want to play another game : (Y/N) ")
        hit_status = Error().in_Error()  
        if hit_status == "n" or hit_status == "N":
            print("Game End")
            print("you have {} Chips in the End of the Game ".format(total_chips.total))
            break
        else:
            print("\n", "Welcome Again!!!!!!!!!!!!", "\n") 

# Import necessary modules
import random
import time
import os

# Define the ranks and suits
ranks: tuple[str] = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits: tuple[str] = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck: list[tuple[str, str]] = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck 
random.shuffle(deck) # since you're boring
 
# Split the deck into two hands
hand1: list[tuple[str, str]] = deck[:int(len(deck) / 2)]
hand2: list[tuple[str, str]] = deck[int(len(deck) / 2):]

# Peacedecks necessary in case peaces are stacked on top of each other
peacedeck1: list = []
peacedeck2: list = []

def screen_clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def card_comparison(p1_card: tuple[str, str], p2_card: tuple[str, str]) -> int:
	"""This is the logic that compares two cards to find the stronger card
	Return 1 if player 1's card is strong, 2 for player 2
	if the cards are equal, return 0.

	Hint, using the index function will make this very simple (one liner)"""
	# Your code here
	if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
		return 1
	elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
		return 2
	else:
		return 0
      
def card_possibility(hand_len1: int, hand_len2: int) -> int:
      """
      Checks how many cards are left in the deck so the peace function can address how many cards to take away.
      """
      if hand_len1 == 0 or hand_len2 == 0:
            return 0
      elif hand_len1 == 1 or hand_len2 == 1:
            return 1
      elif hand_len1 == 2 or hand_len2 == 2:
            return 2
      elif hand_len1 == 3 or hand_len2 == 3:
            return 3
      else:
            return 4

def repeace_time(peacedeck1: list[tuple[str, str]], peacedeck2: list[tuple[str, str]]) -> int:
    print("Reshuffling both player's peace bounty cards until a winner is found...")
    time.sleep(2)
    while True:
        random.shuffle(peacedeck1)
        random.shuffle(peacedeck2)
        if peacedeck1[-1] != peacedeck2[-1]:
            return card_comparison(peacedeck1[-1], peacedeck2[-1])

def peace_winner(hand1: list[tuple[str, str]], hand2: list[tuple[str, str]], state: int) -> None:
    if state == 1:
        print("Looks like Player 1 won this round of peace!")
        for _ in range(len(peacedeck1)): hand1.append(peacedeck1.pop(0))
        for _ in range(len(peacedeck2)): hand1.append(peacedeck2.pop(0))
    elif state == 2:
        print("Looks like Player 2 won this round of peace!")
        for _ in range(len(peacedeck1)): hand2.append(peacedeck1.pop(0))
        for _ in range(len(peacedeck2)): hand2.append(peacedeck2.pop(0))

def play_round(player1_hand: list[tuple[str, str]], player2_hand: list[tuple[str, str]]) -> None:
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the peace function
	"""
    # Your code here
    p1_card: tuple[str, str] = player1_hand[0]
    p2_card: tuple[str, str] = player2_hand[0]
    game_state: int = card_comparison(p1_card, p2_card)
    print(f"Playing cards! Player 1 flipped the {str(p1_card[0])} of {str(p1_card[1])} and Player 2 flipped the {str(p2_card[0])} of {str(p2_card[1])}!")
    if game_state == 0:
        peace(hand1, hand2)
    elif game_state == 1:
        print("Player 1 won this round!")
        hand1.append(hand2.pop(0))
        hand1.append(hand1.pop(0))
    else:
        print("Player 2 won this round!")
        hand2.append(hand1.pop(0))
        hand2.append(hand2.pop(0))

def peace(hand1: list[tuple[str, str]], hand2: list[tuple[str, str]]) -> None: 
    """Handle the 'peace' scenario when cards are equal.
		recall the rules of peace, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here
    input("It's time for peace! Hit 'enter' to continue.")

    cards_possible: int = card_possibility(len(hand1), len(hand2))

    if cards_possible != 1 or (len(peacedeck1) > 0 and cards_possible == 1):
        prev_total: int = 0
        if len(peacedeck1) > 0:
            prev_total = len(peacedeck1) - 1
        for _ in range(cards_possible): peacedeck1.append(hand1.pop(0)) 
        for _ in range(cards_possible): peacedeck2.append(hand2.pop(0))
        print(f"Because {peacedeck1[0 + prev_total][0]} of {peacedeck1[0 + prev_total][1]} and {peacedeck2[0 + prev_total][0]} of {peacedeck2[0 + prev_total][1]} have the same rank, drawing {cards_possible} cards from both decks...")
        time.sleep(1) 
        print(f"Cards drawn! Player 1, your top card is {str(peacedeck1[-1][0])} of {str(peacedeck1[-1][1])}, and Player 2, your top card is {str(peacedeck2[-1][0])} of {str(peacedeck2[-1][1])}.")
        peace_state = card_comparison(peacedeck1[-1], peacedeck2[-1])
        if peace_state == 0:
            cards_possible: int = card_possibility(len(hand1), len(hand2))
            print("Uh oh! Looks like we need to go to peace again!")
            if cards_possible > 0:
                print(f"Looks like an even bigger pot this time, with the winner taking home {len(peacedeck1) + cards_possible} cards this time!")
                peace(hand1, hand2)
            else:
                print("Hey wait a minute! Someone doesn't have enough cards to go to peace again...")
                state = repeace_time(peacedeck1, peacedeck2)
                print(f"Cards drawn! Player 1, your top card is {str(peacedeck1[-1][0])} of {str(peacedeck1[-1][1])}, and Player 2, your top card is {str(peacedeck2[-1][0])} of {str(peacedeck2[-1][1])}.")
                peace_winner(hand1, hand2, state)
        else:
            peace_winner(hand1, hand2, peace_state)
    else:
        print("Someone's last card is the same as the other player's current card!")
        time.sleep(1)
        print("Going to make the player with the most cards pick a new top card!")
        time.sleep(1)
        print("You'll be playing a regular round (if the next card has the same rank, you'll be seeing this again!)")
        time.sleep(1)
        if len(hand1) != 1:
            hand1.append(hand1.pop(0))
        else:
            hand2.append(hand2.pop(0))

def play_game() -> None:
    """Main function to run the game."""
    # Your code here
    input("Let's play a game of Peace! Hit 'enter' to continue.")
    print("Dealing cards to Player 1 and Player 2...")
    time.sleep(3)
    print("Cards dealt! Time to start.")

    while len(hand1) != 0 and len(hand2) != 0:
          print(f"Round has started. Player 1 has {len(hand1)} cards left, and Player 2 has {len(hand2)} cards left.")
          input("Hit 'enter' to play your cards.")
          screen_clear()
          time.sleep(0.5)
          play_round(hand1, hand2)
    
    if len(hand1) == 0:
          print("Player 2 has won this game of Peace! Better luck next time Player 1.")
    else:
          print("Player 1 has won this game of Peace! Better luck next time Player 2.")

# Call the main function to start the game
play_game()
# Import necessary modules
import random
import time

# Define the ranks and suits
ranks: tuple[str] = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits: tuple[str] = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck: list[tuple[str, str]] = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck 
i = 0
randnums = []
shuffleddeck = []
while i < 52:
	temprand = random.randint(0, 51)
	if temprand in randnums:
		continue
	shuffleddeck.append(deck[temprand])
	randnums.append(temprand)
	i += 1
	
#or random.shuffle(deck) if you're boring
 
# Split the deck into two hands
hand1 = shuffleddeck[:26]
hand2 = shuffleddeck[26:]

# Peace decks necessary in case peaces are stacked on top of each other
peacedeck1 = []
peacedeck2 = []

def card_comparison(p1_card, p2_card):
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
      
def card_possibility(hand_len1, hand_len2):
      """
      Checks how many cards are left in the deck so the peace function can address how many cards to take away.
      """
      if hand_len1 >= 4 and hand_len2 >= 4:
            return 4
      elif hand_len1 == 3 or hand_len2 == 3:
            return 3
      elif hand_len1 == 2 or hand_len2 == 2:
            return 2
      elif hand_len1 == 1 or hand_len1 == 1:
            return 1
      else:
           return 0

def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the peace function
	"""
    # Your code here
    p1_card = player1_hand[0]
    p2_card = player2_hand[0]
    game_state = card_comparison(p1_card, p2_card)
    print(f"Playing cards! Player 1 flipped {p1_card} and Player 2 flipped {p2_card}!")
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

def peace(player1_hand, player2_hand):
    """Handle the 'peace' scenario when cards are equal.
		recall the rules of peace, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here
    input("It's time for peace! Hit 'enter' to continue.")

    cards_possible = card_possibility(len(hand1), len(hand2))

    if len(peacedeck1) != 0 or cards_possible != 1:
        for _ in range(cards_possible): peacedeck1.append(hand1.pop(0)) 
        for _ in range(cards_possible): peacedeck2.append(hand2.pop(0))
        print(f"Because {peacedeck1[0]} and {peacedeck2[0]} have the same rank, drawing {cards_possible} cards from both decks...")
        time.sleep(1)
        peace_state = card_comparison(peacedeck1[-1], peacedeck2[-1])
        print(f"Cards drawn! Player 1, your top card is {peacedeck1[-1]}, and Player 2, your top card is {peacedeck2[-1]}.")
        if peace_state == 0:
            print("Uh oh! Looks like we need to go to peace again!")
            if cards_possible == 4:
                print(f"Looks like an even bigger pot this time, with the winner taking home {len(peacedeck1) + 4} cards this time!")
                peace(hand1, hand2)
            else:
                print("Hey wait a minute! Someone doesn't have enough cards to go to peace again...")
                print("Looks like we'll have to reshuffle the top cards and play a normal game!")
                for _ in range(len(peacedeck1)): hand1.append(peacedeck1.pop(0))
                for _ in range(len(peacedeck2)): hand2.append(peacedeck2.pop(0))
                hand1.append(hand1.pop(0))
                hand2.append(hand2.pop(0))
        elif peace_state == 1:
            print("Looks like Player 1 won this round of peace!")
            for _ in range(len(peacedeck1)): hand1.append(peacedeck1.pop(0))
            for _ in range(len(peacedeck2)): hand1.append(peacedeck2.pop(0))
        elif peace_state == 2:
            print("Looks like Player 2 won this round of peace!")
            for _ in range(len(peacedeck1)): hand2.append(peacedeck1.pop(0))
            for _ in range(len(peacedeck2)): hand2.append(peacedeck2.pop(0))
    elif cards_possible == 1:
        print("Someone's last card is the same as the other player's current card!")
        print("Going to make the player with the most cards pick a new top card!")
        print("You'll be playing a regular round (if the next card has the same rank, you'll be seeing this again!)")
        if len(hand1) != 1:
            hand1.append(hand1.pop(0))
        else:
            hand2.append(hand2.pop(0))

def play_game():
    """Main function to run the game."""
    # Your code here
    input("Let's play a game of Peace! Hit 'enter' to continue.")
    print("Dealing cards to Player 1 and Player 2...")
    time.sleep(3)
    print("Cards dealt! Time to start.")

    while len(hand1) != 0 and len(hand2) != 0:
          print(f"Round has started. Player 1 has {len(hand1)} cards left, and Player 2 has {len(hand2)} cards left.")
          input("Hit 'enter' to play your cards.")
          play_round(hand1, hand2)
    
    if len(hand1) == 0:
          print("Player 2 has won this game of Peace! Better luck next time Player 2.")
    else:
          print("Player 1 has won this game of Peace! Better luck next time Player 2.")

# Call the main function to start the game
play_game()
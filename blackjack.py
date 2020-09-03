import random

# Dealer Cards
dealer_cards = []

# Player Cards
player_cards = []

	# Deal the Cards
# Dealer Cards
while len(dealer_cards) != 2:
	dealer_cards.append(random.randint(1, 11))
	if len(dealer_cards) == 2:
		print("Dealer has: ", dealer_cards)

# Sum of the dealer cards 
# Sum of the player cardsCompare the sums of the cards between D v P
# If P card sum is greater than 21 = bust
# If P card sum is less than 21 = Option Hit or Stay
# If P option stay compare sum of D v P 
# If P sum < 21 && > D Sum then P Wins!
# If P sum < D sum then P loses


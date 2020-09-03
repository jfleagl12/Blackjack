import random

# Dealer Cards
dealer_cards = []

# Player Cards
player_cards = []

# Deal the Cards
# Display the cards
# Dealer Cards
while len(dealer_cards) != 2:
	dealer_cards.append(random.randint(1, 11))
	if len(dealer_cards) == 2:
		print("Dealer has X &", dealer_cards[1])

# Player Cards
while len(player_cards) != 2:
	player_cards.append(random.randint(1, 11))
	if len(player_cards) == 2:
		print("You have ", player_cards)

# Sum of the dealer cards
if sum(dealer_cards) == 21:
	print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
	print("Dealer has busted!")

# Sum of the player cards
while sum(player_cards) < 21:
	action_taken = str(input("Do you want to stay or hit? "))
	if action_taken == "hit":
		player_cards.append(random.randint(1,11))
		print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
	else:
		print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
		print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)

# Compare the sums of the cards between D v P
# If P card sum is greater than 21 = bust
# If P card sum is less than 21 = Option Hit or Stay
# If P option stay compare sum of D v P 
# If P sum < 21 && > D Sum then P Wins!
# If P sum < D sum then P loses


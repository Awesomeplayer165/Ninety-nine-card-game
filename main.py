totalPointTotal = 0
playerHand = []
restOfCards = []

# Example:
# 87, 5, 8, 9, 7, 4, 6, 3, 9, 0, 2 - 101, dealer
# 78, 2, 4, 8, 3, 8, 5, 0, 6, 9, 8 - 100, dealer
# 85, 7, 9, 7, 6, 5, 9, 4, 5, 0, 1 - 101, dealer
# 84, 8, 4, 2, 7, 9, 0, 1, 9, 8, 3 - 100, dealer
# 95, 9, 0, 9, 0, 1, 0, 1, 0, 2, 5 - 100, player



def addPoints(n: int) -> int:
	global totalPointTotal

	if   n == 9: totalPointTotal += 0
	elif n == 4: totalPointTotal -= 10
	elif n == 0: totalPointTotal += (11 if totalPointTotal + 11 <= 99 else 1)
	else:        totalPointTotal += n


def getInput():
	global totalPointTotal, playerHand, restOfCards
	
	cards = input("Enter an input: ").replace(" ", "").split(",")

	totalPointTotal = int(cards[0])
	playerHand = [int(cards[1]), int(cards[2]), int(cards[3]), int(cards[4]), int(cards[6]), int(cards[8]), int(cards[10])]
	restOfCards = [int(cards[5]), int(cards[7]), int(cards[9])]


def computeScoreAndWinnerWithCurrentCards() -> (str, int):
	global playerCards, restOfCards

	isPlayerTurn = True

	while totalPointTotal <= 99:
		addPoints(playerHand[0] if isPlayerTurn else restOfCards[0])
		
		if isPlayerTurn: playerHand .pop(0)
		else:            restOfCards.pop(0)

		isPlayerTurn = not isPlayerTurn

		print(f"{totalPointTotal}, {"player" if isPlayerTurn else "dealer"}")

getInput()
print(computeScoreAndWinnerWithCurrentCards().name)
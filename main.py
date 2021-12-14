totalPoints = 0
playerHand = []
dealerCards = []

# Examples:
# 87, 5, 8, 9, 7, 4, 6, 3, 9, 0, 2 - 101, dealer
# 78, 2, 4, 8, 3, 8, 5, 0, 6, 9, 8 - 100, dealer
# 85, 7, 9, 7, 6, 5, 9, 4, 5, 0, 1 - 101, dealer
# 84, 8, 4, 2, 7, 9, 0, 1, 9, 8, 3 - 100, dealer
# 95, 9, 0, 9, 0, 1, 0, 1, 0, 2, 5 - 100, player


def addPoints(n: int) -> int:
	global totalPoints

	if   n == 9: totalPoints += 0
	elif n == 4: totalPoints -= 10
	elif n == 0: totalPoints += (11 if totalPoints + 11 <= 99 else 1)
	else:        totalPoints += n


def getInput():
	global totalPoints, playerHand, dealerCards
	
	userInput = input("Enter an input: ").replace(" ", "").split(",")

	totalPoints = int(userInput[0])
	
	playerHand = [int(userInput[1]), 
								int(userInput[2]), 
								int(userInput[3]), 
								int(userInput[4]), 
								int(userInput[6]), 
								int(userInput[8]), 
								int(userInput[10])]

	dealerCards = [int(userInput[5]), 
								 int(userInput[7]), 
								 int(userInput[9])]


def computeScoreAndWinnerWithCurrentuserInput():
	global playeruserInput, dealerCards, totalPoints

	isPlayerTurn = True

	while totalPoints <= 99:
		addPoints(playerHand[0] if isPlayerTurn else dealerCards[0])
		
		if isPlayerTurn: playerHand .pop(0)
		else:            dealerCards.pop(0)

		isPlayerTurn = not isPlayerTurn

	print(str(totalPoints) + ", " + ("player" if isPlayerTurn else "dealer"))

getInput()
computeScoreAndWinnerWithCurrentuserInput()
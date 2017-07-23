import random 

#"Guess" at a good defense baseline, trying to assign 1.8 soldiers per victory point.
baseline = [0, 2, 4, 6, 7, 9, 11, 13, 14, 16, 18]
# Generated from massScore(createAlternates()), the "winning" defense
trueBestDefense = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Generated from calculateWinOptions().
# Saved here for ease.
win_options = [[0, 0, 0, 0, 0, 0, 0, 0.5, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.5, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.5, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0.5, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0.5, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0.5, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0.5, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0.5, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0.5, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0.5, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1], [0, 0, 0, 0.5, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0.5, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0.5, 1, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0.5, 1, 0, 1, 1, 0, 0, 1], [0, 0, 0, 0.5, 1, 1, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1], [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0.5, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0.5, 0, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0.5, 0, 1, 0, 1, 0, 1, 1, 0], [0, 0, 0.5, 0, 1, 0, 1, 1, 0, 0, 1], [0, 0, 0.5, 0, 1, 1, 0, 0, 1, 0, 1], [0, 0, 0.5, 1, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0.5, 1, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0.5, 1, 0, 1, 0, 0, 0, 1, 1], [0, 0, 0.5, 1, 1, 1, 0, 1, 1, 0, 0], [0, 0, 0.5, 1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1], [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1], [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0], [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]]

def createAlternates():
	possibilities = [baseline];
	for castle in range(1, 10):
		newPossibilities = []
		for modification in xrange(-2, 3):
			for possibility in possibilities:
				newStrength = possibility[castle] + modification
				if possibility[castle - 1] <= newStrength:
					npossibility = list(possibility)
					npossibility[castle] = newStrength
					newPossibilities.append(npossibility)
		possibilities = newPossibilities
		print castle, len(possibilities)
	# Just add up to 100 for the final castle guard
	newPossibilities = []
	for possibility in possibilities:
		possibility[10] = 100 - sum(possibility[:-1])
		newPossibilities.append(possibility)
	print "created: ", len(newPossibilities)
	#a = random.choice(newPossibilities)
	#b = random.choice(newPossibilities)
	#print a, sum(a)
	#print b, sum(b)
	return newPossibilities

def massScore(defenses):
	print "Mass scoring: ", len(defenses)
	bestScore = 0
	winners = []
	for defense in defenses:
		score = scoreDefense(defense)
		if bestScore < score:
			bestScore = score
			winners = [defense]
		elif bestScore == score:
			winners.append(defense)
	print len(winners)
	print bestScore
	a = random.choice(winners)
	b = random.choice(winners)
	c = random.choice(winners)
	print a, b, c

def scoreDefense(defense):
	minSoldiers = 100
	winningOptions = []
	for win_option in win_options:
		totalSoldiers = 0
		for index in xrange(1, 11):
			if win_option[index] == 1:
				totalSoldiers += defense[index] + 1
			elif win_option[index] == 0.5:
				totalSoldiers += defense[index]
		if totalSoldiers < minSoldiers:
			minSoldiers = totalSoldiers
			winningOptions = [win_option]
		elif totalSoldiers == minSoldiers:
			winningOptions.append(win_option)
	print minSoldiers
	print len(winningOptions)
	return minSoldiers


def calculateScore(poss):
	score = 0
	for a in xrange(len(poss)):
		score += poss[a] * a
	return score

def hasTie(poss):
	return 0.5 in poss

def hasWin(poss):
	return 1 in poss

def canBeReduced(poss):
	posscopy = list(poss)
	if hasTie(poss):
		lowTie = poss.index(0.5)
		posscopy[lowTie] = 0
	else:
		lowWin = poss.index(1)
		posscopy[lowWin] = 0.5
	# If we would win anyway despite dropping a bit,
	# this win is "inefficient".
	return calculateScore(posscopy) >= 28

def calculateWinOptions():
	possibilities = [[0]];
	for castle in range(1, 11):
		newPossibilities = []
		for possibility in possibilities:
			alreadyHasTie = hasTie(possibility)
			alreadyHasWin = hasWin(possibility)
			score = calculateScore(possibility)
			npossibility = list(possibility)
			npossibility.append(0)
			newPossibilities.append(npossibility)
			if score < 28:
				if not alreadyHasTie and not alreadyHasWin:
					npossibility = list(possibility)
					npossibility.append(0.5)
					newPossibilities.append(npossibility)
					score = calculateScore(npossibility)
					if score < 28:
						npossibility = list(possibility)
						npossibility.append(1)
						newPossibilities.append(npossibility)
				else:
					npossibility = list(possibility)
					npossibility.append(1)
					newPossibilities.append(npossibility)
		possibilities = newPossibilities

	# filter out losses
	filtered = [x for x in possibilities if calculateScore(x) >= 28]
	# Filter out inefficient wins
	irreduceable = [ x for x in filtered if not canBeReduced(x)]

	irLen = len(irreduceable)
	q = random.choice(irreduceable)
	w = random.choice(irreduceable)
	e = random.choice(irreduceable)

	print q, calculateScore(q)
	print w, calculateScore(w)
	print e, calculateScore(e)
	print fixedLen, irLen
	print irreduceable



if __name__ == "__main__":
    #calculateWinOptions()
    #scoreDefense(baseline)
    scoreDefense(trueBestDefense)
    #massScore(createAlternates())

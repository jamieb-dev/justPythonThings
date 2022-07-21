count = 0

def up1000():
	loopCount = 0
	while True:
		global count
		count += 1
		loopCount += 1
		if loopCount == 1000000:
			print(count)
			break

while True:
	if count == 100000000:
		break
	else:
		up1000()

# TASK: Create workaround for global variable
# TASK: Add highscore recorder in .txt file
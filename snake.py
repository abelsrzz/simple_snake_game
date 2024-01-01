# Imports
import time
import keyboard
import os
import random


# Game difficulty
score = 3
targetNum = 1
speed = .5


# Map size

# X coordinate
mapLength = 30
# Y coordinate
mapHeight = 10


# Player initial position
playerPositionX = mapLength // 2
playerPositionY = mapHeight // 2


# Set player tail
tail = [[playerPositionX, playerPositionY]]


# Targets
targetPositions = []


def generate_targets(targetNum):
    for i in range(0, targetNum):
        targetPositionX = random.randint(1, mapLength - 2)
        targetPositionY = random.randint(1, mapHeight - 2)
        targetPositions.append([targetPositionX, targetPositionY])


# First target generation
generate_targets(targetNum)


# Duplication and consecutive deletion functions
def has_duplications(arr):
    seen = set()
    for sub_list in arr:
        sub_tuple = tuple(sub_list)
        if sub_tuple in seen:
            return True
        seen.add(sub_tuple)
    return False


def delete_consecutive(arr):
    result = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:
            result.append(arr[i])
    return result


# Set key for auto-movement
lastPressed = "d"

while True:

    # Store player position
    playerPositionArray = [playerPositionX, playerPositionY]
    # Store shown tail
    shownTail = tail[-score:]

    # Error correction
    shownTail = delete_consecutive(shownTail)

    # Store head position
    head = shownTail[-1]

    scoreFlag = 0
    for y in range(0, mapHeight):
        if y == 0 or y == mapHeight - 1:
            # Print map delimitation
            print("+ " * mapLength)
        else:
            headFlag = 0
            for x in range(0, mapLength):
                # Print map delimitation
                if x == 0:
                    print("+", end=" ")
                elif x == mapLength - 1:
                    print("+", end="\n")
                else:
                    targetFlag = 0
                    # Print targets
                    for targetPrint in targetPositions:
                        if playerPositionArray == targetPrint:
                            scoreFlag = 1
                        if targetPrint[0] == x and targetPrint[1] == y:
                            targetFlag = 1
                    if targetFlag == 1 and scoreFlag == 0:
                        print("*", end=" ")
                    else:
                        printTaleFlag = 0
                        # Print tale
                        for snake in shownTail:
                            headFlag = 0
                            if snake[0] == x and snake[1] == y:
                                printTaleFlag = 1
                                if snake == head:
                                    headFlag = 1
                        # Print head and tale
                        if headFlag == 1:
                            print("O", end=" ")
                        elif printTaleFlag == 1:
                            print("x", end=" ")
                            headFlag = 1
                        else:
                            print(" ", end=" ")
    # Score storage
    if scoreFlag == 1:
        targetPositions = []
        generate_targets(targetNum)
        score += 1
        speed = (score // 3) * speed
    # print("Player pos ", playerPositionArray)
    # print("Player tail: ", shownTail)
    # print("Target positions: ", targetPositions)
    print("Player score: ", score)
    print("Press [q] for quit.")

    # Keypress detection
    if keyboard.is_pressed("w"):
        lastPressed = "w"
    elif keyboard.is_pressed("s"):
        lastPressed = "s"
    elif keyboard.is_pressed("d"):
        lastPressed = "d"
    elif keyboard.is_pressed("a"):
        lastPressed = "a"
    elif keyboard.is_pressed("q"):
        exit(0)

    # Movement
    if lastPressed == "w":
        playerPositionY -= 1
    elif lastPressed == "s":
        playerPositionY += 1
    elif lastPressed == "d":
        playerPositionX += 1
    elif lastPressed == "a":
        playerPositionX -= 1

    # Map end fix
    if playerPositionX == 0:
        playerPositionX = mapLength - 2
    elif playerPositionY == 0:
        playerPositionY = mapHeight - 2
    elif playerPositionX == mapLength - 1:
        playerPositionX = 1
    elif playerPositionY == mapHeight - 1:
        playerPositionY = 1

    # Tail storage
    tail.append([playerPositionX, playerPositionY])

    # Game over
    if has_duplications(shownTail):
        print("Game Over!")
        exit(0)

    # Speed declaration
    time.sleep(speed)

    # Screen clean
    if os.system("cls"):
        continue
    else:
        os.system("clear")

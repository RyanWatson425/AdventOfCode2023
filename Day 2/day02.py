fileContents = open(r"C:\development\AdventOfCode2023\Day 2\data\data.txt")
fileContentsList = fileContents.readlines()

# PART 1 SOLUTION
# gameIdSum = 0
# for game in fileContentsList:
#     gameTitle, gameResults = game.split(': ')
#     gameId = int(gameTitle[5:])
#     gameResultsList = gameResults.split("; ")
#     isPossible = True
#     for gameResult in gameResultsList:
#         colorsDrawn = gameResult.split(", ")
#         for colorQuantity in colorsDrawn:
#             quantity, color = colorQuantity.split(' ')
#             if color.find('red') > -1:
#                 if int(quantity) > 12:
#                     isPossible = False
#             elif color.find('green') > -1:
#                 if int(quantity) > 13:
#                     isPossible = False
#             else:
#                 if int(quantity) > 14:
#                     isPossible = False
#     if isPossible:
#         gameIdSum += gameId

# print(gameIdSum)


# PART 2 SOLUTION

minimumCubesPower = 0
for game in fileContentsList:
    gameTitle, gameResults = game.split(': ')
    gameId = int(gameTitle[5:])
    gameResultsList = gameResults.split("; ")
    isPossible = True
    maxRedCubesFound = 1
    maxGreenCubesFound = 1
    maxBlueCubesFound = 1
    for gameResult in gameResultsList:
        colorsDrawn = gameResult.split(", ")
        for colorQuantity in colorsDrawn:
            quantity, color = colorQuantity.split(' ')
            if color.find('red') > -1:
                maxRedCubesFound = max(int(quantity), maxRedCubesFound)
            elif color.find('green') > -1:
                maxGreenCubesFound = max(int(quantity), maxGreenCubesFound)
            else:
                maxBlueCubesFound = max(int(quantity), maxBlueCubesFound)
    minimumCubesPower += maxBlueCubesFound * maxRedCubesFound * maxGreenCubesFound

print(minimumCubesPower)
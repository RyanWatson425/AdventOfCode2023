fileContents = open("data/data.txt", "r")
fileContentsList = fileContents.readlines()

runningTotal: int = 0
# PART 1 SOLUTION
# for line in fileContentsList:
#     leftPtr: int = 0
#     rightPtr: int = len(line) - 1
#     while not line[leftPtr].isdigit():
#         leftPtr = leftPtr + 1
#     while not line[rightPtr].isdigit():
#         rightPtr = rightPtr - 1

#     runningTotal = runningTotal + (int(line[leftPtr]) * 10) + int(line[rightPtr])

# print(runningTotal)


# PART 2 SOLUTION
for line in fileContentsList:
    leftNumValue: int
    rightNumValue: int

    leftPtr = 0
    numArray: list = []
    while leftPtr < len(line):
        #checking strings of size 1 for numbers
        if line[leftPtr].isnumeric():
            numArray.append(int(line[leftPtr]))
            
        #checking strings of size 3 for numbers
        if leftPtr + 2 < len(line):
            threeSlice = line[leftPtr:leftPtr + 3]
            if threeSlice == "one":
                numArray.append(1)
            elif threeSlice == "two":
                numArray.append(2)
            elif threeSlice == "six":
                numArray.append(6)

        #checking strings of size 4 for numbers
        if leftPtr + 3 < len(line):
            fourSlice = line[leftPtr:leftPtr + 4]
            if fourSlice == "four":
                numArray.append(4)
            elif fourSlice == "five":
                numArray.append(5)
            elif fourSlice == "nine":
                numArray.append(9)

        #checking strings of size 5 for numbers
        if leftPtr + 4 < len(line):
            fiveSlice = line[leftPtr:leftPtr + 5]
            if fiveSlice == "three":
                numArray.append(3)
            elif fiveSlice == "seven":
                numArray.append(7)
            elif fiveSlice == "eight":
                numArray.append(8)

        leftPtr = leftPtr + 1
        
    leftNumValue = numArray[0]
    rightNumValue = numArray[-1]
    runningTotal = runningTotal + leftNumValue * 10 + rightNumValue

print(runningTotal)
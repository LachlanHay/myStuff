'''
Read a list of integers from user input.
Find all pairs of numbers in the list whose product is even and whose sum is odd.
Print out a formatted list of the pairs.
'''

# Read list of integers from user input
intList = []
userInput = ''

print("Enter 'end' to stop list input")
while userInput != "end":
    userInput = input("Enter integer for list: ")

    if userInput != 'end':
        userInput = int(userInput)
        intList.append(userInput)

# Find all pairs of numbers in the list whose product is even and whose sum is odd
pairsList = []

# check pairs
pos1 = 0
while pos1 in range(len(intList)):

    # multiply/add int1 to other list items
    int1 = intList[pos1]

    pos2 = 0
    while pos2 in range(len(intList)):
        # don't want to use same list index for second number
        if pos2 != pos1:
            int2 = intList[pos2]

            if (int1 * int2)%2 == 0:
                pairsList.append([int1, int2])

            if (int1 + int2)%2 == 1:
                pairsList.append([int1, int2])

        pos2 += 1

    pos1 += 1


# format list so that there are no duplicate pairs
for index in range(len(pairsList) - 1):
    if pairsList[index] == pairsList[index+1]:
        pairsList[index+1] = None

# print out formatted list of the pairs
formattedList = []
for index in range(len(pairsList)):
    if pairsList[index] != None:
        formattedList.append(pairsList[index])

print(formattedList)




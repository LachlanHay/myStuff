# Sorting Practice

def selectionSort():

    enum = len(aList)
    # go through list elements, swap min_num
    
    for i in range(enum): # for going through sorted list.
        min_index = i
        for j in range(i+1, enum): # swap for smallest num in unsorted list
            if aList[j] < aList[min_index]:
                min_index = j

                
        temp = aList[i]
        aList[i] = aList[min_index] 
        aList[min_index] = temp
                
    print(aList)

def countingSort():

    bit_list = [0] * 10
    for index in bList:
        bit_list[index] += 1

    new_list = []
    for index in range(len(bit_list)):
        if index > 0:
            for j in range(bit_list[index]):
                new_list.append(index)
            
    print(new_list)

def insertionSort():

    n = len(cList)
    for i in range(1, n):
        j = i
        while cList[j-1] > cList[j] and j>0:
            temp = cList[j-1]
            cList[j-1] = cList[j]
            cList[j] = temp
            j = j-1
    print(cList)

aList = [5, 8, 3, 4, 2, 9, 2]
bList = aList.copy()
cList = aList.copy()

selectionSort()
countingSort()
insertionSort()

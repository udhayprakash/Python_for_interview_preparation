# Implementing Binary Search algorithm in Python

# Binary Search is a method to look for an item in a sorted sequence. It works by comparing the target item to middle-indexed element of the sequence;
# if unequal, the half of the sequence in which the target cannot lie is discarded, and process is repeated on the remaining half until target item is found or until the sequence is exhausted.

# PSEUDO CODE

##set beginningIndex to 0
##set endingIndex to (length of sequence - 1)
##set targetElement to target value
##set targetElementFound to False
##
##while targetElementFound is not True:
##    calculate middleIndex of sequence as beginningIndex + endingIndex // 2
##
##    if targetElement is located at data[middleIndex]:
##        success
##    else:
##        if value of targetElement is less than value at data[middleIndex]:
##            set endingIndex to middleIndex - 1
##        else:
##            set beginningIndex to middleIndex + 1

# Sample Data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

beginningIndex = 0
endingIndex = len(data) - 1
targetElement = 8
targetElementFound = False
iterationNo = 1

while targetElementFound is not True:
    print("Iteration {}; beginningIndex: {}; endingIndex: {}".format(iterationNo, beginningIndex, endingIndex))

    middleIndex = (beginningIndex + endingIndex) // 2
    if targetElement == data[middleIndex]:
        targetElementFound = True
        print("Element {} found at index {}.".format(targetElement, middleIndex))
    else:
        if targetElement <= data[middleIndex]:
            endingIndex = middleIndex - 1
        else:
            beginningIndex = middleIndex + 1

    iterationNo += 1

## OUTPUT ##
##Iteration 1; beginningIndex: 0; endingIndex: 8
##Iteration 2; beginningIndex: 5; endingIndex: 8
##Iteration 3; beginningIndex: 7; endingIndex: 8
##Element 8 found at index 7.

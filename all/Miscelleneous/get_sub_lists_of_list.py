listOne = [1,2,3,4]
 
subLists = [ [] ]           # initializing a list of sublists with an empty list
 
for lowerBoundOfSlice in range(len(listOne)):                   # for lowerBoundOfSlice in 0 to 3
    upperBoundOfSlice = lowerBoundOfSlice + 1              
    while upperBoundOfSlice <= len(listOne):                 # while upperBoundOfSlice is < or = 4
        subList = listOne[lowerBoundOfSlice:upperBoundOfSlice]  # obtaining a sublist using bounds
        subLists.append(subList)                                # appending sublist to list containing sublists
        upperBoundOfSlice += 1                                  # incrementing upperBoundOfSlice
 
print(subLists)         # [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]
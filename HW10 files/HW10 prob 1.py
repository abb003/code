def findItem(inputList, item):
    index = [0]
    
    while item in inputList:
        if index == item:
            print('item found')
        else:
            index += 1

        if index == item:
            return item
        else:
            return -1

lst1 = findItem(['1', '2', '3'], '2')
print(lst1)

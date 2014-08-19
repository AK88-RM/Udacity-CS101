def symmetric(mylist):
    if mylist == []:           # check from empty set
        return True
    rows = len(mylist)         # check length of rows versus columns
    columns = len(mylist[0])
    if columns != rows:
        return False
    i = 0
    j = 0
    for row in mylist:
        print 'row', row
        column = []
        for element in row:      # compose column
            list1 = mylist[i]
            cell = list1[j]
            column.append(cell)
            i = i+1
        print 'column', column
        i = 0
        j = j + 1
        if row != column:    # check row entry = column entry
            return False
    return True

#print symmetric([[1, 2, 3],
#                [2, 3, 4],
#                [3, 4, 1]])
#>>> True

print symmetric([])

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False

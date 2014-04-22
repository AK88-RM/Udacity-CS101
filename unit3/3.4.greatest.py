def greatest(list1):
    biggest = 0
    for element in list1:
        if element > biggest:
            biggest = element
    return biggest


#print greatest([4,23,1])
#>>> 23
print greatest([])
##>>> 0

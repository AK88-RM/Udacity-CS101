def list_mean(l):
    if l == []:
        return 0
    length = len(l)
    sum = 0
    for entry in l:
        sum = sum + entry
    mean = float(sum) / length 
    return mean


print list_mean([1,2,3,4])
#>>> 2.5
print list_mean([1,3,4,5,2])
#>>> 3.0
print list_mean([])
#>>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print list_mean([2])
#>>> 2.0

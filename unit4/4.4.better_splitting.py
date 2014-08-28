def split_string(source,splitlist):
    stringlist = []
    entry = []
    i = 0
    n=0
    m=0
    while n < len(source):
        while i < len(splitlist):
            if source[n] == splitlist[i] or n+1 == len(source):
                entry = source[m: n]
                if n+1 == len(source):
                    if source[n] not in splitlist:
                        entry = source [m: n+1]
                if entry != '':
                    stringlist.append(entry)
                m = n + 1
            i = i + 1
        i = 0 
        n = n + 1
    return stringlist


out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']



         

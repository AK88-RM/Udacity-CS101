def numbers_in_lists(string):
    bignum = 0
    num = 0
    result = []
    junior = []
    for i in range (0, len(string)):
        num = int(string[i])
        #print "num ", num, "oldnum ", oldnum
        if num <= bignum:
            junior.append(num)
        else:
            if junior != []:
                result.append(junior)
                junior = []
            result.append(num)
            bignum = num
    if junior != []:
        result.append(junior)
    print result
    return result

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result

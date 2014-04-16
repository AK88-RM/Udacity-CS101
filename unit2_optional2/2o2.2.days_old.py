# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
    
def totaldays(year, month, day):
    num = (year-1)/4 - (year-1)/100 + (year-1)/400 # extra leap year days
    yr_d = (year-1) * 365 + num  # total days in years up to start of year.

    mt_d = 0  # total days in months up to start of month
    i = 0
    while i < month-1:
        i = i + 1
        if ((i == 4) or (i == 6) or (i == 9) or (i == 11)):
            mt_d = mt_d + 30
        elif (i == 2):
            mt_d = mt_d + 28
            if isLeapYear(year):
                mt_d = mt_d + 1
        else: 
            mt_d = mt_d + 31
    return (yr_d + mt_d + day)
        


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    d1 = totaldays(year1, month1, day1)
    d2 = totaldays(year2, month2, day2)
    print d2-d1
    return d2-d1


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

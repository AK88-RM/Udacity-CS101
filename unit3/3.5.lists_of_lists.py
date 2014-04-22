udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(list1):
    totstu = 0
    tottut = 0
    while list1:
        list2 = list1.pop()
        totstu = totstu + list2[1]
        tottut = tottut + list2[1] * list2[2]
    return totstu, tottut







#print total_enrollment(udacious_univs)
#>>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside 
# interpreter you might not see it.

#print total_enrollment(usa_univs)
#>>> (77285,3058581079L)

# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    # your code here
    if day[0] == ('S' or 's'):
        if day[1:] == 'aturday' or 'unday':
            return True
    return False

#print weekend('Monday')
#>>> False

#print weekend('Saturday')
#>>> True

#print weekend('July')
#>>> False	

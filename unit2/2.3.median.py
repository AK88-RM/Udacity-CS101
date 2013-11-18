# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    n = biggest(a,b,c)
    if n == a:
        return bigger(b,c)
    if n == b:
        return bigger(a,c)
    return bigger(a,b)

# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(s,t):
    i = s.find(t)
    if i != -1:
        while True:
            if s.find(t,i+1) == -1:
                return i
            i = i + 1
    return i

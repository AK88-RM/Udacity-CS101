# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
def abacus(value):
    line = ""
    length = 0
    i = 0
    sym = str(0)
    while length < 11:
        if length < (10-value):
            symbol =  sym
            i =i+1
        elif (10-value) <= length < (11-value):
            symbol = '   '
        else:
            symbol = sym
            i=i+1
        line = line + symbol
        if i == 5:
            sym = '*'
        length = length + 1
    return line

          #  print "|" + abacus(num) +  "|"



def print_abacus(value):
        line ="00000*****"
        i=10
        while i>0:
            num = (value / (10 ** (i-1))) % 10          
            print "|" + line[0:10-num] + "   " + line[10-num:] + "|"
            i = i - 1
        return
            

###  TEST CASES
#print "Abacus showing 0:"
#print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#print "Abacus showing 12345678:"
#print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
#print "Abacus showing 1337:"
#print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|

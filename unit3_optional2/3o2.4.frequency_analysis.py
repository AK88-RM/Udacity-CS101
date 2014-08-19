def freq_analysis(message):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    freq_list = [0.0]*26
    for i in message:
        print i, abc.find(i), freq_list[abc.find(i)]
        freq_list[abc.find(i)] = freq_list[abc.find(i)] + (1.0/len(message))
    #print abc, freq
    #print len(message)
    return freq_list



#Tests

#print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

#a 0 0.0
#d 3 0.0
#c 2 0.0
#a 0 0.25
#[0.5, 0.0, 0.25, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]

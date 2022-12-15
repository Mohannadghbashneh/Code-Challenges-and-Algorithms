# Write here the code challenge solution
from collections import Counter
 
def first_word_Repeat(input):
    list = input.split(' ')
    dict = Counter(list)
    for key in list:
        if dict[key]>1:
            return key
    else:
     return 'No Repetition'
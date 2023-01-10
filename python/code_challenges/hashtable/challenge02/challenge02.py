# Write here the code challenge solution
def first_repeated_word(str1):
  l=str1.split()
  temp = set()
  for word in l:
    if word in temp:
      return word
    else:
      temp.add(word)
  return 'No Repetition'
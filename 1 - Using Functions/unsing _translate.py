from string import  maketrans

filename = "abcdefghija"

# make a traduction of each char in the string
print filename.translate(maketrans("abcdefghij","1234567890"))
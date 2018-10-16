#atbash cipher
import string

def atbash(password):
    ascending = string.ascii_lowercase
    descending = ascending[::-1]
    letterdict = {}
    for position in range(len(ascending)):
        letterdict[ascending[position]] = descending[position]
    output = ""
    for letter in password:
        if letter in letterdict:
            output += letterdict[letter]
        else:
            output += letter
    return output

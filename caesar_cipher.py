#caesar decipher
import string

def decipher(text, offset=1):
    test_dict = {}
    letters = string.ascii_lowercase
    #generate offset mapping using dictionary
    for position in range(len(letters)):
        test_dict[letters[position]] = letters[(position+offset)%len(letters)]
    #print output using mapping
    output = ""
    for letter in text:
        if letter in test_dict:
            output += test_dict[letter]
        else:
            output += letter
    return output

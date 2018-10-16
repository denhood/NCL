import base64 as b64

def decrypt(password, base=16):
    if base == 16: #compute hexadecimal character equivalents
        for charsequence in range(0,len(password),2):
            print(chr(int(password[charsequence:charsequence+2], base)),end="")
    if base == 64:
        #calculate base 64
        print(b64.b64decode(password))
    if base == 2:
        #remove any spaces in character sequence
        password = password.replace(" ","")
        for charsequence in range(0,len(password),8):
            print(chr(int(password[charsequence:charsequence+8], base)),end="")

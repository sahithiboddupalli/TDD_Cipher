class Cipher(object):
    def encrypt(self, string, shift):
        res = ''
        for char in string: 
            if char.islower():
                res+= chr((ord(char) + shift - 97) % 26 + 97)
            elif  char.isupper():
                res+= chr((ord(char) + shift - 65) % 26 + 65)
            elif char.isdigit():
                res+= char
            elif char == ' ':
                res+= char
            else:
                res+ = char
        return res
        
    def decrypt(self, string, shift):
        res = ''
        for char in string: 
            if char == ' ':
                res+= char
            elif char.islower():
                res+= chr((ord(char) - shift - 97) % 26 + 97)
                print(ord(char), ord(char)-shift-97, (ord(char) - shift - 97)%26, (ord(char) - shift - 97) % 26 + 97)
            elif  char.isupper():
                res+= chr((ord(char) - shift - 65) % 26 + 65)
            elif char.isdigit():
                res+= char
            else:
                res+= char
        return res

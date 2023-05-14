def encrypt(text):
    text = text[::-1]
    letterList = list(text)
    wordCount = len(letterList)
    #text = ''.join(letterList)
    letterList = list(text)
    for x in range(wordCount):
        asciiLetter = ord(letterList[x])
        if asciiLetter >= 81 and asciiLetter <= 90 or asciiLetter >= 113 and asciiLetter <= 122:
            letterList[x] = asciiLetter - 16
        else:
            letterList[x] = asciiLetter + 10
        letterList[x] = chr(letterList[x])
    text = ''.join(letterList)
    return text
                
        
def decrypt(text):
    letterList = list(text)
    for x in range(len(letterList)):
        asciiLetter = ord(letterList[x])
        if asciiLetter <= 74 or asciiLetter >= 97 and asciiLetter <= 106:
            letterList[x] = asciiLetter + 16
        else:
            letterList[x] = asciiLetter - 10
        letterList[x] = chr(letterList[x])
    text = ''.join(letterList)
    text = text[::-1]
    return text

# Main program
file1 = open("plainText.txt", "r")
file2 = open("encryptedText.txt", "w" )
file1.seek(0)
stringCount = len(file1.readlines())
file1.seek(0)
for x in range(stringCount):
    word = str(file1.readline().splitlines([0])
    word = encrypt(word)
    file2.write(word + "\n")
    print("enrypted word: " + word + "\n")
file2.close()
file2 = open("encryptedText.txt", "r" )
for x in range(stringCount):
    word = str(file2.readline().splitlines()[0])
    word = decrypt(word)
    print("decrypted word: " + word + "\n")  
file1.close()
file2.close()



































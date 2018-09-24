
string = "Jryy V unq n ovt oheevgb ng Puvcbgyr'f naq vg jnf tbbq."
ch = 0
translated = ''
while ch < len(string):
    origin_letter = string[ch]
    if origin_letter.isalpha():
        alphabet = ord(origin_letter) + 13
        if chr(ord(origin_letter)).isupper():
            if alphabet > ord('Z'):
                alphabet -= 26
            elif alphabet < ord('A'):
                alphabet += 26
        elif chr(ord(origin_letter)).islower():
            if alphabet > ord('z'):
                alphabet -= 26
            elif alphabet < ord('a'):
                alphabet += 26
        finalLetter = chr(alphabet)
        translated += finalLetter
    
    else:
        translated += string[ch]
    ch += 1     
print(translated, end='')   
       
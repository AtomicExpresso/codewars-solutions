def rot13(message):
    answer = []
    
    for i, char in enumerate(message):
        charCode = ord(char)
        
        if (charCode >= 65 and charCode <= 90): # uppercase chars
            answer.append(chr(((charCode -65 + 13) % 26) + 65))
        elif (charCode >= 97 and charCode <= 122): # lowercase chars
            answer.append(chr(((charCode -97 + 13) % 26) + 97))
        else: # non-alphabetic chars
            answer.append(message[i])
            
    return "".join(answer)

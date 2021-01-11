def validBraces(string):
    
    pass

#how to test for interlocking brackets of different species

ch = "({)}"

i = 0

if (ch.count('(') + ch.count('{') + ch.count('[')) == (ch.count(')') + ch.count('}') + ch.count(']')):

    while i < len(ch):
        if (ch[i] == '(') and (ch[i+1] == ('}' or ']')):
            print(False)
            break

        elif (ch[i] == '[') and (ch[i+1] == (')' or '}')):
            print(False)
            break

        elif (ch[i] == '{') and (ch[i+1] == (')' or ']')):
            print(False)
            break
        else:
            print(True)
            break
else:
    print(False)

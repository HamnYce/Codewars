
#how to test for interlocking brackets of different species

# ch = "({)}"

# i = 0
# #first check to see if bracket count is valid


# if (ch.count('(') + ch.count('{') + ch.count('[')) == (ch.count(')') + ch.count('}') + ch.count(']')):

#     while i < len(ch):
#         if (ch[i] == '(') and (ch[i+1] == ('}' or ']')):
#             print(False)
#             break

#         elif (ch[i] == '[') and (ch[i+1] == (')' or '}')):
#             print(False)
#             break

#         elif (ch[i] == '{') and (ch[i+1] == (')' or ']')):
#             print(False)
#             break
#         else:
#             print(True)
#             break
# else:
#     print(False)

#answer provided @M7md_isk on Codewars
def validBraces(string):
    left = ["(","[","{"]
    right = [")","]","}"]
    seen = []
    
    for bracket in string:
        if bracket in left:
            seen.append(bracket)
        else:
            if len(seen) == 0:
                return False
            if left[right.index(bracket)] == seen[-1]:
                seen.pop()
        
    if len(seen) > 0:
        return False
    else:
        return True
    pass
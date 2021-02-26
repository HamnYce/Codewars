# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:
#https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python


def solution(string,markers):
    newtext = ""
    stringlist = string.split("\n")
    for line in stringlist:
        for i in markers:
            if i in line:
                newtext += (line[0:line.index(i)]).strip() + "\n"
                break
        else:
            newtext += line + "\n"
        
    for i in markers:
        newtext = newtext.strip(i)
    return newtext
    
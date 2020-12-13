# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)


def iq_test(numbers):
    j = 0
    odd = 0
    even = 0
    numbers = numbers.split()
    
    for i in numbers:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
            
    while j < len(numbers):
        if even >= 2:
            if int(numbers[j]) % 2 != 0:
                position = j + 1
        else:
            if int(numbers[j]) % 2 == 0:
                position = j + 1
        j += 1
    return position

print(iq_test("1 3 4 7 9"))


#https://www.codewars.com/kata/reviews/55322529855bcccee70000b0/groups/5532da092f8863dfbc00005f
#puts everything on one level and then manipulates it
def iq_test(numbers):

    #converts string to list of true and falses whhere true is even and false is odd
    e = [int(i) % 2 == 0 for i in numbers.split()]
    

    #returns the index of true if its the only one, i.e. only even
    #else it returns the index of false, i.e. only odd number... clever..
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
#some criticisms towards this code is of perfomance.
#the function goes throgh the list twice
#a solution for this is to check only the first 3 elements as that would be enough to distinguish the odd one out:
#e.index(True) if e[:3].count(False) > 1 else e.index(False)
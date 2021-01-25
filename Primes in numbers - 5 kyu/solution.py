# Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form
#  "(p1**n1)(p2**n2)...(pk**nk)"

#  where a ** b means a to the power of b

# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"


#Divide by smallest prime number possible, then restart the loop, repeat with increasing size of prime number when previous ones return nothing
#Need list of prime numbers
#print "(primenumber**numberoftimes)"

#https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python

# def prime_factors(n):
#     primefactors = []
#     while n > 1:
    
#         for num in range(2,100):
#             for i in range(2,num):
#                 if num%i == 0:
#                     break
#             else:
#                 #in this stage we have our smallest prime number
#                 #print(num)
#                 while n % num == 0:
#                     n /= num
#                     primefactors.append(num)
#                     print(num)
#     return ''.join("({}**{})".format(i,primefactors.count(i)) if primefactors.count(i) > 1 else "({})".format(i) for i in set(primefactors))

# print(prime_factors(77754609000))


def prime_factors(n):
    pm100 = []
    newpms = []
    for num in range(2,265371653):
        for i in range(2,num):
            if num%i == 0:
                break 
        else:
            pm100.append(num)
    print("next step")
    while n > 1:
        for i in pm100:
            while n % i == 0:
                n /= i
                newpms.append(i)

    return ''.join("({}**{})".format(i,newpms.count(i)) if newpms.count(i) > 1 else "({})".format(i) for i in sorted(set(newpms)))


print(prime_factors(7775460044540))

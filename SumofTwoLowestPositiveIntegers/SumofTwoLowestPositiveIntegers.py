def sum_two_smallest_numbers(numbers):
    numbers.sort()
    bin = numbers[0] + numbers[1]
    
    
    return bin


print(sum_two_smallest_numbers([3,5,1,6,2]))


#https://www.codewars.com/kata/reviews/57a075cf8ac8e75966000109/groups/57a0a743cf1fa5595a0003f6
#def sum_two_smallest_numbers(numbers):
    #return sum(sorted(numbers)[:2])\

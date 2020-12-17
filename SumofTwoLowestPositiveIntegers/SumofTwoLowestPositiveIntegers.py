def sum_two_smallest_numbers(numbers):
    numbers.sort()
    bin = numbers[0] + numbers[1]
    
    
    return bin


print(sum_two_smallest_numbers([3,5,1,6,2]))

a = ("bc", "ba", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)
def square_digits(num):
    num = str(num)
    squarednum = ""
    for i in range(len(num)):
        squarednum += str((int(num[i]) ** 2))
    squarednum = int(squarednum)

    return squarednum





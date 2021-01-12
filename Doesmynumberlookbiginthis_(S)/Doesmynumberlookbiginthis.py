


def narcissistic( value ):
   
    narc = 0

    for i in str(value):
        narc += int(i) ** len(str(value))

    return value == narc


#ive just learned that you can use for loops inside return statements! As well as if and else, i wonder about while loops...
#anyways, this was the top answer after submission enjoy some genius too

#def narcissistic(value):
 #   return value == sum(int(x) ** len(str(value)) for x in str(value))


# string = "chocolate is gucci good"
# stringlist = string.split()
# reversedd = ""


# for word in stringlist:

#     if len(word) >= 5:
#         word = word [::-1] 

#         reversedd += word

#     else:
#         reversedd += word
#     reversedd += " "
# reversedd = reversedd.strip()

def spin_words(sentence):
    ls = sentence.split(' ')
    for wordindex in range(len(ls)):
        if len(ls[wordindex]) >= 5:
            ls[wordindex] = ls[wordindex][::-1]
    return ' '.join(ls)

print(spin_words("chocolate is springs"))


# Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine;
#  there are no other people in the queue.
# The first one in the queue (Sheldon) buys a can, drinks it and doubles!
# The resulting two Sheldons go to the end of the queue.
# Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.

# For example, Penny drinks the third can of cola and the queue will look like this:

# Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
# Write a program that will return the name of the person who will drink the n-th cola.


queue = ["Howard", "Rajesh", "Penny", "Leonard", " Sheldon"]
pueue = [1,2,3,4,5]
pueue5 = [1,1,2,2,3,3,4,4,5,5]
pueue15 = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5]
pueueu35 = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5]
n = 75
for i in range(n):
    queue.insert(0,queue[-1])
    queue.insert(0,queue[-1])
    queue.pop()
print(queue)
# geometric sequence, every step is increasting by 
#0 (1 copy), 5 (2 copies),15 (4 copies),35 (8 copies),75 (16 copies),155 (32 copies),315 (64 copies)
# +5,+10,+20,+40,+80,+160


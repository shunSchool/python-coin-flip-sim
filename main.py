#python coin flip simulator

import random

#totals
num_heads = 0
num_tails = 0

n = 1
while n <= 10:
    #flip a coin
    randNum = random.randrange(1, 3)
    if randNum == 1:
        print("heads")
        num_heads += 1
    else:
        print("tails")
        num_tails += 1

    #increment n
    n += 1
print("H:" + str(num_heads))
print("T:" + str(num_tails))
print("goodbye jojo!!!")

# use a for loop to run  a set # of times
#for n in range(10):
#    print("hi")

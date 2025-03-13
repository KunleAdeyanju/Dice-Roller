from random import randrange
# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#

a = int (input("How many die to you want to roll\n"))

mylist = []
def dice_roll(x):
    for i in range(x):
        mylist.append(randrange(6))

dice_roll(a)

print("These are your rolls: ") 
print(*mylist, sep=', ')
# for s in mylist:
    # print(s)
#print(mylist)



        


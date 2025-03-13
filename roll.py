from random import randrange
# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#



mylist = []
def dice_roll(x):
    for i in range(x):
        mylist.append(randrange(6))

keep_playing = True

while keep_playing:
    a = int (input("How many die to you want to roll\n"))
    dice_roll(a)

    print("These are your rolls: ") 
    print(*mylist, sep=', ')

    t = input("\nDo you want to keep playing? Y/N\n").lower()
    if t == "n":
        keep_playing = False
    elif t == "y":
        keep_playing = True
        mylist = []
    else:
        print("That wasn't an option womp womp game over")
        keep_playing = False
# for s in mylist:
    # print(s)
#print(mylist)



        


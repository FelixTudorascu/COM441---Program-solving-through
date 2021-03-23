book_cover = input("What type of cover does the book have? ( Soft or Hard )\n")

if ( book_cover == 'soft'):
    book_type = input("Is the book perfect-bound?\n")
    if ( book_type == 'yes'):
        print("Soft cover, perfect bound books are very popular!")
    elif ( book_type == 'no'): 
        print("Soft covers with coils or stitches are great for short books")
elif ( book_cover == 'hard'):
    print("Books with hard covers can be more expensive!")
#========================

answer = input("Where should I look?\n")

if ( answer == "in the bedroom" ):
    answer = input("Where in the bedroom should I look?\n")
    if ( answer == "under the bed" ):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")
elif ( answer == "in the bathroom" ):
    anwer = input("Where in the bathroom should I look?\n")
    if ( answer == "in the bathtub\n" ):
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")
elif ( answer == "in the lab" ):
    answer = input("Where in the lab should I look?\n")
    if ( answer == "on the table" ):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
else:
    print("I do not know where that is but I will keep looking.")


#=====================
adventure_type = input("What type of adventure should I have?\n")

if ( adventure_type == 'scary' or adventure_type == 'short'):
    print("Entering the dark forest!")
elif ( adventure_type == 'safe' or adventure_type == 'long'):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")


#=================
response_answer = input("What did i hear ? \n")
response1_answer = input("What did i see? \n")

if ((response_answer == "grr") and (response1_answer == "two red eyes")):
  print("There is a scary creature. I should get out of here!")

else:
  print("I am a little scared but I will continue.")

#===============
answer = int(input("How many cable should i remove? \n"))

x = 0

while (x < answer):
  print("removed cable")
  x= x + 1


#===================
answer = int(input("How many live cables must i avoid? \n"))

x = 1

while ( x <= answer ):
    print(f"Avoiding... Done! {x} live cables Avoiding ")
    x += 1
print("All live cables have been avoided.")



#===================

import random

print("Oh wow look ! A field !")
print(" We should go looking for some four leafed clovers , for good luck!")
print( )
print(" But ohh .... the grass is the same colour as them ... looks like you're gonna have to guess where they are ")

clover = random.randint (0,15)

# the loop starts here !
for i in range(15):
    choice= input(" Look there ! Choose a location (number) on the grass and pick it !")
    if choice == clover:
        # if you win , this is where the loop ends !
        print(" We found one ! Thats amazingly good luck for years !")
        quit()
    else:
        print()
        print(" Thats a piece of grass ! Try again !")

# if you didn't win , the loop ends here .
print()
print(" Looks like you didn't find one ... that sounds like bad luck for you .")
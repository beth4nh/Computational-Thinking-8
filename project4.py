import random

print("Oh wow look ! A field !")
print(" We should go looking for some four leafed clovers , for good luck!")
print( )
print(" But ohh .... the grass is the same colour as them ... looks like you're gonna have to guess where they are ")

clover = random.randint (0,15)

# the loop starts here ! If you win , it ends on line 17 .

for i in range(15):
    
    choice = int(input(" Look there ! Choose a location (number) on the grass and pick it !"))
    if choice == clover:
        print(" We found one ! Thats amazingly good luck for years !")
        quit()
    
    else:
        wrong = random.randint (1,5)
        
        if wrong == 1:
            print()
            print(" Thats a piece of grass ! Try again !")
        if wrong == 2:
            print()
            print(" Try again , thats a piece of grass ...")
        if wrong == 3:
            print()
            print(" Im sure you're close . . . ! ")
        if wrong == 4:
            print()
            print(" HOLD ON I THINK THATS ONE NEXT TO IT ! GRAB IT !")
        if wrong == 5:
            print()
            print(" c'mon ... i gotta get home soon ....")

# if you didn't win , the loop ends here .
print()
print(" Looks like you didn't find one ... that sounds like bad luck for you .")
print(" But it's okay. theres always next time !")

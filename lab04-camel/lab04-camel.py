import random
import arcade

arcade.open_window(800, 600, "Camel")

def main():

    miles=0
    thirst=0
    tire=0
    natives=-20
    canteen=3

    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    done = False
    while not done:
        print ("A. Drink from your canteen.")
        print ("B. Ahead moderate speed.")
        print ("C. Ahead full speed.")
        print ("D. Stop for the night.")
        print ("E. Status check.")
        print ("Q. Quit\n", " ")

        respuesta=input("What is your choice? ")

        print (" ")

# ------------------------------THIRST---------------------------------------------#
        if thirst > 4 and thirst < 7: print ("You are thirsty")

        if thirst > 6:
            print ("You died of thirst")
            done = True


# -------------------------------TIRED---------------------------------------------#
        if tire > 5 and tire < 9 and not done: print("Your camel is getting tired")

        if thirst > 8 and not done:
            print("Your camel is dead")
            done = True
# -------------------------------NATIVES-------------------------------------------#
        if miles-natives < 15 and not done: print ("The natives are getting close!")

        if natives == miles and not done:
            print ("The navites caught you")
            done = True


# ---------------------------------WIN---------------------------------------------#
        if miles >= 200 and not done:
            print ("VICTORY!")
            done = True


# -------------------------------OASIS---------------------------------------------#
        if random.randint(1,100)<=20:
            print ("Oasis!")
            print ("Canteen refilled, thirsty reseted and camel rested")
            canteen=3
            thirst=0
            tire=0


# -------------------------------BUCLE---------------------------------------------#
        if respuesta.upper()=="Q":
            done = True
            print ("THE END")

        elif respuesta.upper() == "E":
            print("-------------------------------------------------------------")
            print ("Miles: " , miles)
            print ("Canteen: " , canteen)
            print ("The natives are ", miles-natives , " miles behind you.")
            print("-------------------------------------------------------------")

        elif respuesta.upper() == "D":
            tire=0
            print("-------------------------------------------------------------")
            print ("The camel is happy")
            print("-------------------------------------------------------------")
            natives+=random.randint(7,14)

        elif respuesta.upper() == "C":
            miles+=random.randint(10,20)
            print("-------------------------------------------------------------")
            print("Total miles: ", miles)
            print("-------------------------------------------------------------")
            thirst+=1
            tire+=random.randint(1,3)
            natives+=random.randint(7,14)

        elif respuesta.upper() == "B":
            miles+=random.randint(5,12)
            print("-------------------------------------------------------------")
            print ("Total miles: ", miles)
            print("-------------------------------------------------------------")
            thirst+=1
            tire+=1
            natives+=random.randint(7,14)

        elif respuesta.upper() == "A":
            if canteen!=0:
                canteen-=1
                thirst=0
                print("-------------------------------------------------------------")
                print ("Thirst set to 0")
                print("-------------------------------------------------------------")
            else: print ("No drinks left")

        print(" ")

main()
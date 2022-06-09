
#this make sure the number inputted is an interger and not a decimal
#aswell as making sure the number is between 80 and 100 if not fail message
while True:
    B = input ("Enter a temperature that water begins boils at, so input something between 80 to 200 degrees celcius:")
    if B.isdigit():
        B = int (B)
        if B > 80 and B < 200:
            break
        else:
            print("That's not a temperature between 80 to 200 degrees celcius")
    else:
        print("that's a decimal, try putting an integer")
#your formula
P = 5 * B - 400
#now since I have P I can see if it's above or below sea level
if (P) > 100:
    print("The atmospheric pressure is " + str(P) + "kPa, Below sea level")
else:
    if (P) < 100:
        print("The atmospheric pressure is " + str(P) + "kPa, Above sea level")

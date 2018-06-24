print("Welcome! This program is designed to make your math homework easier! ")
print("Would you like to calculate the perimeter or area of your REGULAR polygon?")

def perimeter():
    print("number of sides, side length")
    parameters = input().split(",")
    try:
        print("Perimeter:", int(parameters[0])*int(parameters[1]))
    except:
        print("Try again.")
        perimeter()

def area():
    print("number of sides, side length, distance from a side length to the center")
    parameters = input().split(",")
    try:
        print("Area:", int(parameters[1])*int(parameters[2])/2*int(parameters[0]))
    except:
        print("Try again.")
        area()

def calculate(pOrA):
    print("Please enter the following parameters of your REGULAR shape in the SAME UNITS: ")

    if(pOrA == "Perimeter"):
        perimeter()
    elif(pOrA == "Area"):
        area()
    else:
        print("Try again. 'Perimeter' or 'Area'?")
        pOrA = input()
        calculate(pOrA)

def repeat():
    print("Would you like to try another shape? 'Yes' or 'No'")
    yOrN = input()
    if(yOrN == "Yes"):
        print("Type 'Perimeter' or 'Area' to be prompted with further instructions")
        pOrA = input()   
        calculate(pOrA)
        repeat()
    elif(yOrN == "No"):
        print("Goodbye")
        quit()
    else:
        print("Sorry, I don't understand.")
        repeat()

print("Type 'Perimeter' or 'Area' to be prompted with further instructions")
pOrA = input()   
calculate(pOrA)
repeat()

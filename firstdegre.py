print("This programm will help us to resolve an equation of second degre using the if else condition")
print("#########################################################################################")
a=int(input("Please enter the value of a : "))
b=int(input("Please enter the value of b : "))
if a == 0 :
    print("Impossible, a must be different at 0")
elif b == 0 :
     print("Impossible, b must be different at 0")
else :
    print("The result is : ", -b/a)
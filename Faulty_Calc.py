
print("Addition is a")
print("Subtraction is s")
print("Multiply is m")
print("Division is d")
print("Enter your choice")

Choice = str(input())

print("Enter first number")
First = float(input())
print("Enter second number")
Second = float(input())

if Choice == 'a' and First == 56 and Second == 9:
    print(77)

elif Choice == "a":
    print(First + Second)

elif Choice == "s":
    print(First - Second)

elif Choice == 'm' and First == 45 and Second == 3:
    print(555)

elif Choice == "m":
    print(First * Second)

elif Choice == 'd' and First == 56 and Second == 6:
    print(4)

elif Choice == "d":
    print(First / Second)

elif Choice != "a" "s" "m" "d":
    print("Enter valid key")

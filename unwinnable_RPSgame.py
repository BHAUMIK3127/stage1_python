rock = "rock"
paper = "paper"
scissors="scissors"

print("ROCK , PAPER OR SCISSORS?")

a=input()

while True:
    if a =="rock" :
        print("PAPER HAHA I WIN")

    if a =="paper" :
        print("SCISSORS HAHA I WIN")

    if a =="scissors" :
        print("ROCK HAHA I WIN")

    print("still wanna continue?")

    print("Y FOR YES , N FOR NO")

    choice = ""


        
    choice = input()
    choice.capitalize()

    if choice == "N":
        break
    if choice == "Y":
        continue

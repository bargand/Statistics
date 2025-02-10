"""
Create a program that allows the user to guess a secret number between 1 and 100. The program should keep prompting the user until they guess the correct number.
"""

Sec_Number = 50

while True:
    User_Number = int(input("Guess A Number: "))
    if (0 <= User_Number <= 100):
        if (User_Number > Sec_Number) :
            print("Please decrease your number")
        elif (User_Number < Sec_Number):
            print("Please Increase your number")
        elif(User_Number == Sec_Number):
            print("Congratulation 🥳 🥳 Your Guess is Right")
            break
        else:
            print("I do not understand your number")
    else:
        print("your number is not in between 0 and 100")
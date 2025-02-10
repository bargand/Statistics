"""
i = 1
while i <= 10:
    print(i)
    i+=1
"""
Sec_Number = 50

while True:
    User_Number = int(input("Guess A Number: "))
    if (User_Number > Sec_Number) :
        print("Please decrease your number")
    elif (User_Number < Sec_Number):
        print("Please Increase your number")
    elif(User_Number == Sec_Number):
        print("Congratulation 🥳 🥳 Your Guess is Right")
        break
    else:
        print("I do not understand your number")
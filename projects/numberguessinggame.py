import random
import math

mini=int(input("enter the minimum value to start:"))
high =int(input("enter the maximum value to get end:"))

x=random.randint(mini,high)

print("You have only got 5 chances")

count=0

while count<5:
    count+=1

    guess =int(input("enter a number for guessing:"))


    if x==guess:
        print("you have got it!,Congratulations")

        break
    elif x>guess:
        print("you have guessed too small")
    elif x<guess:
        print("you have guessed too high")
print("The actual number is :",x) 
if count>=5:
    print("you have tried too many times")
    print("try again later")

print("Thankyou for playing")

name=input("enter your name:")
print("Hello!"+ name ,"welcome to my game")
enterance= input("Do you wanna play?")
if enterance.lower() =="yes":
    print("lets play:)")
else:
    quit()
score=0
answer=input("what is meant by cpu? ")
if answer.lower() =="central processing unit":
    print("your answer is correct!")
    score+=1
else:
    print("try again")
answer1=input("who is the founder of java? ")
if answer1.lower()=="james goslin":
    print("your answer is correct!")
    score+=1
else:
    print("try again")
answer2=input("what is a string?")
if answer2.lower()=="sequence of character":
    print("your answer is correct!")
    score+=1
else:
    print("try again")
answer3=input("why do we use int data type?")
if answer3.lower()=="to store numerical values":
    print("your answer is correct!")
    score+=1
else:
    print("try again")
answer4=input("what is meant by stack?")
if answer4.lower()=="last in first out":
    print("your answer is correct!")
    score+=1
else:
    print("try again")
print("the quiz ends")
print(name,"you have scored "+str(score),"thank you for playing")
import random

def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))

def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))

def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is {0}; that's a good time to start programming!".format(age))

def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())

    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())
        print('Completed, have a nice day!')
        print('.................................')
        print('.................................')
        print('.................................')

def game():
    sample=["rock","paper","scissor"]
    comp=random.randint(0,2)  
    compChoice=sample[comp]
    finish=False
    compScore=0
    userScore=0
    while(finish==False):
        
        user=(input("Enter your choice r:rock p:paper s:scissor -->  "))
        if(user not in ["r","p","s"]):
            print("Enter a valid input")
        if((user=="r" and compChoice=="rock")|(user=="p" and compChoice=="paper")|(user=="s" and compChoice=="scissor")):
            print("Computer's Choice is ",compChoice)
            print("OHHH its a tie, nice fight")

        elif((user=="r" and compChoice=="paper")|(user=="p" and compChoice=="scissor")|(user=="s" and compChoice=="rock")):
            print("Computer's Choice is ",compChoice)
            print("I win ") 
            compScore+=1  
        else:
            print("Computer's Choice is ",compChoice)
            print("Congrats you won")
            userScore+=1
        choice=input("Do you wanna fight again : y-->yes n-->no : ")
        if(choice=="n"):
            finish=True
            print("Your score is " ,userScore)
            print("My score is",compScore)
            
            if(userScore>compScore):
                print("You won the fight")
            elif(userScore<compScore):
                print("I won the fight")
            else:
                print("OHH !! its a tie ")
                



def end():
    print('Congratulations, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
    input()

# greet('TE-Chatbot', '2022') # change it as you need
# remind_name()
# guess_age()
# count()
game()
# test()
# end()

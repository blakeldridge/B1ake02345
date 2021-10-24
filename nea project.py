import sys #imports
import random

#variables
score = 0
wrongs = 0

#functions
def check():#checks for amount of wrongs and exits program at 2
    if wrongs >= 2:
        print("you have breached your limit of wrongs")
        print("You scored: ",score)
        scoresave()
        leaderboard()
        print("Thank you for playing my NEA project :D")
        input("press ENTER to leave: ")
        sys.exit()#exits quiz after 2 wrongs
    else:
        pass

def leaderboard(): #code that presents the leaderboard in correct order
    file=open("scores.txt","r")
    readfile = file.readlines()
    sortedData = sorted(readfile,reverse=True)#sorts out data in file and makes it from highest to lowest

    print("TOP 5 SCORES!")
    print("POS\tPOINTS,Name")

    for line in range(5):#shows 5 scores
        print(str(line+1)+"\t"+str(sortedData[line]))


def accountlog():#script for login and registration
    reg = 0
    while reg < 1: #whilst the user hasnt entered correct details it will keep asking for them to login or register
        file = open("login.txt")
        log = input ("Do you have an account? y/n : ")
        if log == 'n':#register script
            username = input("Please enter a new username?:  ")
            password = input("Please enter a new password:  ")
            file = open("login.txt" ,"a")
            file.write(username +"\n")
            file.write(password + "\n")
            file.close()
            print("Your details have been saved")
        if log == "y":#login script
            file = open("login.txt","r")
            username = input("What is your username?: ")
            password = input("What is your password?: ")
            with open("login.txt") as openfile:
                for line in openfile:
                    for part in line.split():
                        if username in part:#checks if username is in file
                            print("Username correct")
                            reg = reg + 1
                        if username not in part:
                            print("Username incorrect")
                            for line in openfile:
                                for part in line.split():
                                    if password in part:#checks if password is in file
                                        print("Login successful")
                                        



def scoresave():#saves your scores onto a scores file
    global score
    if score < 10:#if the score is single digit it adds a leading 0
        score = str(score)
        score = score.zfill(2)
    else:
        score = str(score)
    scoref = open("scores.txt","a")
    scoref.write(str(score) + ':' + user + ',\n')#saves score with username
    scoref.close()


def question():#questions script
    guesses = 0
    global score
    global wrongs
    file = open("songs.txt","r")
    randomNum = random.randint(0, (file_len-1))#gets a random number from lines in songs file
    line = file.readlines()[randomNum]#randomly gets a line from song script
    data = line.split(",")
    while guesses < 2:
        print('Artist/Band: ',data[0])
        question = input("what is the name of the song:").lower()
        if question == data[1]:
            print("correct")
            if guesses == 0:
                score = score + 3
                guesses = 2
            else:
                score = score + 1
                guesses = 2
        else:
            guesses = guesses + 1
            if guesses == 2:
                wrongs = wrongs + 1
                print("That is incorrect :( ")
                check()
            else:
                pass

#intoduction and authorisation
print("Welcome to my NEA project...\nThis is a music game...")
accountlog()

user = input("Enter your alias: ")
#rules
print("\nHow to play:")
print("The Artist/Band name will be displayed,\nthen the intials and amount of letters of the song name will appear")
print("Your job is to guess the songs name :D")
print("good luck and have fun, get the highest score possible")

#calls in the questions function for each line in the text file
file_len = sum(1 for line in open("songs.txt"))#finds how many lines in songs file
with open("songs.txt","r")as file:
    for i in range(10):#asks the question 10 times
        question()


#outputs users score
scoresave()
leaderboard()

print("thank you for playing my NEA project :D")
input("press ENTER to leave: ")




        

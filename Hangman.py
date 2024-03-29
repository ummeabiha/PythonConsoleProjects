import random

print("******************** WELCOME TO HANGMAN ********************")
list_of_words=["biryani","pulao","burger","pasta","lasgna","pizza","hamburger","sausages",
                "karachi","lahore","islamabad","turkey","istanbul","canada","indianocean","manchester",
                "stylo","khaadi","oaks","ideas","mcdonalds","kfc","saya","sohaye","diners","pizzahut","burgerlab"]

word_list=[]
word=random.choice(list_of_words)

for i in word:
    word_list.append(i)

word_length=len(word)

global help
if word_length<=4:
    help = 1
    print("HELP LINE : You have ",help," help!")
elif word_length>=5:
    help = 2
    print("HELP LINE : You have ",help," helps!")
elif word_length>=8:
    help = 3
    print("HELP LINE : You have ",help," helps!")
print("Type 'help' to use Helpline!")

attempts=9
print("Total Attempts: ",attempts)

if word in ["biryani","pulao","burger","pasta","lasgna","pizza","hamburger","sausages"]:
    print("Word Hint: Food Item")
elif word in ["karachi","lahore","islamabad","turkey","istanbul","canada","indianocean","manchester"]:
    print("Word Hint: City or a Country")
elif word in ["stylo","khaadi","oaks","ideas","mcdonalds","kfc","saya","sohaye","diners","pizzahut","burgerlab"]:
    print("Word Hint: Brand or Food Outlet")

print("\nGuess The Word!")
print("Word:  ",end="")

spaces=[]
for i in range(word_length):
    dash= "_"
    spaces.append(dash)

print(spaces)

def hangman():
    if count==1:
        print("+---+"
              "\n|    "
              "\n|    "
              "\n|    "
              "\n|    "
              "\n|    "
              "\n ====''' ")
    elif count==2:
        print("+---+"
              "\n|  | "
              "\n|    "
              "\n|    "
              "\n|    "
              "\n|    "
              "\n ====''' ")

    elif count==3:
        print("+---+"
              "\n|  | "
              "\n|  | "
              "\n|    "
              "\n|    "
              "\n|    "
              "\n ====''' ")

    elif count == 4:
        print("+---+"
              "\n|  | "
              "\n|  | "
              "\n|  o "
              "\n|    "
              "\n|    "
              "\n ====''' ")
    elif count==5:
        print("+---+"
              "\n|  | "
              "\n|  | "
              "\n|  o  "
              "\n|  |  "
              "\n|    "
              "\n ====''' ")
    elif count==6:
        print("+---+"
              "\n|  | "
              "\n|  | "
              "\n|  o  "
              "\n|  |\  "
              "\n|    "
              "\n ====''' ")
    elif count == 7:
        print("+---+"
              "\n|  | "
              "\n|  | "
              "\n|  o  "
              "\n| /|\  "
              "\n|    "
              "\n ====''' ")
    elif count==8:
        print("+---+"
              "\n|  | "
              "\n|  | "
              "\n|  o  "
              "\n| /|\  "
              "\n|   \ "
              "\n ====''' ")
    else:
        print("+---+"
              "\n|  | "
              "\n|  | "
              "\n|  o  "
              "\n| /|\ "
              "\n| / \  "
              "\n ====''' ")
        print("OOPS!! You're Hanged..")


global count
count=0
def word_guessing():
        global count
        if guess in word and guess!="" and guess!=word:
            no = word.count(guess)
            print(guess, " is in the word!")
            print("Correct! There is/are", no, guess, "in the word")

            for i in range(word_length):
                list.clear()
                pos = word.find(guess, i)
                if i == pos:
                    # print(guess, pos)
                    list.append(guess)
                    list.append(int(pos))

                    spaces[(list[1])] = list[0]
            print("WORD: ",spaces)

        else:
            print(guess, " is not in the word!")
            count+=1
            hangman()


list=[]
helpcount=0
word_for_help=[]

i=1
while i<10:
    if spaces!=word_list:
        print("\n ATTEMPT: ", i)
        guess=str(input("Enter your guess: ")).lower()

        if guess=="help":
            helpcount+=1

            if help==1:
               print("WARNING! You have no help left..")
               if helpcount >1:
                   continue
               else:
                   guess = random.choice(word)
                   word_guessing()

            elif help==2:
                if helpcount==1:
                    print("WARNING! You have 1 help left..")
                    guess = random.choice(word)
                    word_guessing()
                elif helpcount > 2:
                    print("WARNING! You have no help left..")
                else:
                    print("WARNING! You have no help left..")
                    guess = random.choice(word)
                    word_guessing()
            else:
                if helpcount==1:
                    print("WARNING! You have 2 helps left..")
                    guess = random.choice(word)
                    word_guessing()
                elif helpcount==2:
                    print("WARNING! You have 1 help left..")
                    guess = random.choice(word)
                    word_guessing()
                elif helpcount > 3:
                    print("WARNING! You have no help left..")
                else:
                    print("WARNING! You have no help left..")
                    guess = random.choice(word)
                    word_guessing()
        else:
            word_guessing()
    else:
        break

    i+=1

if spaces==word_list:
    print("\n************* CONGRATULATIONS! YOU GUESSED IT RIGHT *************")
    print("The Word is", word)
    quit()
else:
    print("\n************* BETTER LUCK NEXT TIME *************")
    print("+---+"
          "\n|  | "
          "\n|  | "
          "\n|  o  "
          "\n| /|\ "
          "\n| / \  "
          "\n ====''' ")
    print("OOPS!! You're Hanged..")
    print("Attempts Exceeded")
    print("THE WORD WAS :", word)


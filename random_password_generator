import random
import math

print("RANDOM PASSWORD GENERATOR")
special_characters= ['!','@','#','$','%','^','&','*','{','}','[',']','-','=']
capital_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small_letters=[]
for i in capital_letters:
    small_letters.append(i.lower())
numbers=['1','2','3','4','5','6','7','8','9']

def choice():
    user_input = str(input("Select Categories:\n(a)Easy\n(b)Medium\n(c)Hard\n(d)Exit Game\n")).strip().lower()

    if user_input=='d':
        quit()

    else:
        if (user_input=='a'):
            random_capital = random.sample(capital_letters, 6)
            random_small = random.sample(small_letters, 6)

            password=(random_capital+random_small)
            random.shuffle(password)
            return(''.join(password))


        elif user_input=='b':
                random_capital = random.sample(capital_letters, 4)
                random_small = random.sample(small_letters, 4)
                random_num = random.sample(numbers, 4)

                password=(random_capital+random_small+random_num)
                random.shuffle(password)
                return (''.join(password))

        elif user_input=='c':
            random_capital = random.sample(capital_letters, 3)
            random_small = random.sample(small_letters, 3)
            random_num = random.sample(numbers, 3)
            random_pun = random.sample(special_characters, 3)

            password=(random_capital+random_small+random_num+random_pun)
            random.shuffle(password)
            return(''.join(password))

        else:
            print("Enter a valid choice")
            choice()

print(choice())
print("Want to generate another password (Y/N)")
tryagain= input(str()).strip().upper()
if tryagain=='Y':
    choice()
else:
    quit()

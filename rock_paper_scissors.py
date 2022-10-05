import random
print("******************** WELCOME TO ROCK PAPER SCISSORS GAME ********************")
que=str(input("Do you want to play with the Computer or with Player_2 ? (Computer/Player2)\n")).title()
turns=int(input("How many turns you want to take? "))
player1_scores=[]
player2_scores=[]

for i in range(1,turns+1):
    print("********* ROUND: ",i," ********")
    print("PLAYER1 TURN :")
    player1_turn=str(input("Choose Rock,Paper or Scissors? ")).title()
    print(que.upper(),"TURN :")
    if que=="Player2":
        player2_turn=str(input("Choose Rock,Paper or Scissors? ")).title()
    else:
        list=["Rock","Paper","Scissors"]
        player2_turn=random.choice(list)
        print("Choose Rock,Paper or Scissors? ",player2_turn)

    if player1_turn=="Rock" and player2_turn=="Rock":
        print("It's a tie!\n")
    elif player1_turn == "Paper" and player2_turn == "Paper":
        print("It's a tie!\n")
    elif player1_turn == "Scissors" and player2_turn == "Scissors":
        print("It's a tie!\n")

    elif player1_turn=="Rock" and (player2_turn=="Paper" or player2_turn == "Scissors"):
        print("Player1 wins in round ",i," !\n")
        player1_scores.append(int(1))
    elif player1_turn == "Paper" and player2_turn == "Rock":
        print("Player1 wins in round ",i," !\n")
        player1_scores.append(int(1))
    elif player1_turn == "Scissors" and player2_turn == "Paper":
        print("Player1 wins in round ", i, " !\n")
        player1_scores.append(int(1))

    elif player2_turn == "Rock" and (player1_turn == "Paper" or player1_turn == "Scissors"):
        print(que," wins in round ",i," !\n")
        player2_scores.append(int(1))
    elif player2_turn == "Scissors" and player1_turn == "Paper":
        print(que," wins in round ", i, " !\n")
        player2_scores.append(int(1))
    elif player2_turn == "Paper" and player1_turn == "Rock":
        print(que," wins in round ", i, " !\n")
        player2_scores.append(int(1))

    elif player1_turn=="" and (player2_turn=="Paper" or player2_turn=="Scissors" or player2_turn=="Rock"):
        print("Player1 missed its turn in this round\n")
        print(que," wins in round ", i, " !\n")
        player2_scores.append(int(1))
    elif player2_turn=="" and (player1_turn=="Paper" or player2_turn=="Scissors" or player2_turn=="Rock"):
        print(que," missed its turn in this round\n")
        print("Player1 wins in round ", i, " !\n")
        player1_scores.append(int(1))
    elif player1_turn=="" and player2_turn=="":
        print("Both Players missed their turns in this round\n")

scores1=sum(player1_scores)
scores2=sum(player2_scores)
print("**************** Final Result ****************")
print("Player1 Obtained ", scores1, " scores")
print(que," Obtained ", scores2, " scores\n")
if scores1>scores2:
   print(" Congratulations Player1 Wins The Game \n")
   print(que,"  Better Luck Next Time !")
elif scores2>scores1:
    print(" Congratulations ",que," Wins The Game \n")
    print(" Player1 Better Luck Next Time !")
else:
    print("It's a Tie!")
print("Play Again !, Byee")

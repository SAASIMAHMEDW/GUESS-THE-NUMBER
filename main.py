"""    ~ DOCUMENTATION ~
AUTHOR : AHMED-ORACLE
DATE : 09 | 01 |2023
PROGRAM : A SIMPLE GAME 
"""
#getting the random value
from random_number import rand_num
#import random_number 
import colorama
import time
import termcolor
#print(r_num)
#print(random_number.r_num)
print ("\n")
termcolor.cprint("\t GUESS THE NUMBER BY AHMED-ORACLE","magenta",attrs=["bold"])
print(colorama.Fore.BLACK+"  "+"<"+"-"*36+">"+"\n")
print(colorama.Fore.RED+" READ CAREFULLY :)"+colorama.Fore.BLACK)
print("•IT'S A SIMPLE "+colorama.Fore.CYAN+"GAME"+colorama.Fore.BLACK)
print("•WHERE YOU HAVE TO "+colorama.Fore.CYAN+"GUESS THE CORRECT NUMBER"+colorama.Fore.BLACK)
print("•YOU HAVE "+colorama.Fore.CYAN+"LIMITED CHANCES"+colorama.Fore.BLACK)
print("•TO GUESS THE "+colorama.Fore.CYAN+"CORRECT NUMBER"+colorama.Fore.BLACK)
print("•RANDOM NUMBER GENERATED\n•IN BETWEEN "+colorama.Fore.CYAN+"1 TO 100"+colorama.Fore.BLACK)
print("•TOTAL CHANCES"+colorama.Fore.CYAN+" 7\n"+colorama.Fore.BLACK)

print("TO START THE GAME PLEASE ENTER \n"+colorama.Fore.CYAN+"(EN) FOR ENTER"+colorama.Fore.BLACK+" // "+colorama.Fore.CYAN+"(EX) FOR EXIT\n"+colorama.Fore.RESET)
start_game = input("=>").upper()
#print("\n")
#global guessesLeft

#assigning the rand_num() function's value into r_num
r_num = rand_num()

if start_game == "EN":
	totalGuesses = 7
	gameOver = 0
	numberOfGuessesTook = 0
	print("\nTOTAL GUESSES ",totalGuesses)
	while True:
		totalGuesses = totalGuesses - 1
		guessesLeft = totalGuesses
		numberOfGuessesTook+=1
		print("\nENTER YOUR GUESSED NUMBER")
		user_guessed_num = int(input("=>"))
		if guessesLeft == gameOver:
			print("GMAE OVER")
			print("YOU ARE OUT OF CHANCES")
			break
		elif user_guessed_num == r_num:
			print("CONGRATULATIONS\nYOU HAVE GUESSED CORRECT")
			print(f"YOU TOOK {numberOfGuessesTook} CHANCE(S)")
			break
		elif user_guessed_num > r_num:
			
			print("TOO HIGH")
			print("GUESSES LEFT ",guessesLeft)
		elif user_guessed_num < r_num:
			#guessesLeft = totalGuesses -1
			print("TOO LOW")
			print("GUESSES LEFT ",guessesLeft)
		# elif totalGuesses == gameOver:
		# 	print("GAME OVER ")
		#else:
			#print("I AM ELSE")
			#break
	
elif start_game == "EX":
	print(colorama.Fore.RED+"\nYOU HAVE ENTERED EXIT")
else:
	print(colorama.Fore.RED+"\nYOU HAVE ENTERED WRONG PROMT")


# global totalGuesses 
# totalGuesses = 7
# totalGuesses = totalGuesses - 1
# guessesLeft = totalGuesses
# numberOfGuessTook = None
# gameOver = 0
# if totalGuesses == gameOver:
# 	print("gamePver")
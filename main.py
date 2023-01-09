"""    ~ DOCUMENTATION ~
AUTHOR : AHMED-ORACLE
DATE : 09 | 01 |2023
PROGRAM : A SIMPLE GAME 
"""

from random_number import r_num
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
print("•TOTAL CHANCES"+colorama.Fore.CYAN+" 7\n"+colorama.Fore.BLACK)

print("TO BEGIN THE GAME PLEASE ENTER \n"+colorama.Fore.CYAN+"(EN) FOR ENTER"+colorama.Fore.BLACK+" // "+colorama.Fore.CYAN+"(EX) FOR EXIT\n"+colorama.Fore.RESET)
start_game = input("=>").upper()
#print("\n")
if start_game == "EN":

	while True:
		print("\nENTER YOUR GUESSED NUMBER")
		user_guessed_num = int(input("=>"))
		#print ("\n")
		if user_guessed_num == r_num:
			print("CONGRATULATIONS\nYOU HAVE GUESSED CORRECT")
			break
		elif user_guessed_num > r_num:
			print("TOO HIGH")
		elif user_guessed_num < r_num:
			print("TOO LOW")
		#else:
			#print("I AM ELSE")
			#break
elif start_game == "EX":
	print("YOU HAVE ENTERED EXIT")
else:
	print("YOU HAVE ENTERED WRONG PROMT")


# global totalGuesses 
# totalGuesses = 7
# guessesLeft = totalGuesses - 1
# numberOfGuessTook = None
# gameOver = 0
# if totalGuesses == gameOver:
# 	print("gamePver")
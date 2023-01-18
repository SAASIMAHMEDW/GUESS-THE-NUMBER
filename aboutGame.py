import termcolor
import colorama

def about_game():
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

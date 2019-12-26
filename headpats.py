from colorama import Fore, Style, deinit, init

init()

print(Fore.BLUE + Style.BRIGHT + 'Lemme patpat youuuuu -w- do u wanna some headpats ? [Yes/No]')
plop = input()

if plop == "Yes":
	print("Patpatpatpatpatpatpat >w<")
elif plop == "No":
	print("Oh... ;w;")
else :
	print("Uhm, okay :thinking:")

deinit()
exit()

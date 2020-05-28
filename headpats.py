from colorama import Fore, Style, deinit, init
import time
import random
import signal

init()

class TimerException(Exception):
    pass

def timeout(a,b):
    raise TimerException("TIMEOUT")


def randchoice():
    t = random.choice(["Automatic choice = headpats !!! *patpatpatpatpatpatpat* >w<", "Automatic choice = Huggyyyyyyys !!! *huggy* >w<", "Automatic choice = Nothing : go to hell."])
    print(t)

signal.signal(signal.SIGALRM, timeout)

signal.alarm(5)

try:
    inp = input(Fore.BLUE + Style.BRIGHT + 'Lemme patpat youuuuu -w- do u wanna some headpats ? [Y/N].\r\nCountdown before an automatic choice : 5sec.\r\n')
except TimerException:
    inp = randchoice()

print()

if inp == "Y":
    print(Fore.RED + Style.BRIGHT + "Patpatpatpatpatpatpat >w<")
elif inp == "N":
    try:
        inp  = input(Fore.GREEN + Style.BRIGHT + "Oh... Mh, some huggys ? *^* [Y/N/Maybe]\r\n")
    except TimerException:
        inp = "default"
    print()
    if inp == "Y":
        print(Fore.RED + Style.BRIGHT + "Huggyyyyyyys !!!")
    if inp == "N":
        print(Fore.YELLOW + Style.BRIGHT + "\'kay...")
    if inp == "Maybe":
        print("Pfff, are you braindead ?")

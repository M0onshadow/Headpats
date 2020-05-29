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
    x = ["Headpats !!! *patpatpatpatpatpatpat* >w<", "Huggyyyyyyy !!! *hug* >w<", "Nothing : go to hell."]
    t = Fore.MAGENTA + "I've chosen for you !\r\n" + random.choice(x)
    print(t)

signal.signal(signal.SIGALRM, timeout)

signal.alarm(7)

try:
    inp = input(Fore.BLUE + Style.BRIGHT + 'Lemme patpat you ! Do u wanna some headpats ? [Y/N].\r\nCountdown before an automatic choice : 7sec.\r\n')
except TimerException:
    inp = randchoice()

print()

if inp == "Y":
    print(Fore.RED + Style.BRIGHT + "Patpatpatpatpatpatpat >w<")
elif inp == "N":
    try:
        inp  = input(Fore.GREEN + Style.BRIGHT + "Oh... Mh, some huggys ? *^* [Y/N]\r\n")
    except TimerException:
        inp = "default"
    print()
    if inp == "Y":
        print(Fore.RED + Style.BRIGHT + "Huggyyyyyyys !!!")
    if inp == "N":
        print(Fore.YELLOW + Style.BRIGHT + "\'kay...")

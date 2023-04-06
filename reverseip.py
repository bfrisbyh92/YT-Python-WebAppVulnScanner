from requests import get
from colorama import Fore, Back

cyan = Fore.CYAN
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW


def ReverseIP():
    host = input(Back.BLACK + Fore.CYAN + "Enter host >> ")
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
    try:
        result = get(lookup).text
        print(cyan+"[+]"+result)
    except:
        print(red+'Invalid IP address')


if __name__ == "__main__":
    ReverseIP()

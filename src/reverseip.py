from requests import get
from colorama import Fore, Back
from urllib.parse import urlparse

cyan = Fore.CYAN
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW


def ReverseIP(url):
    print(Fore.BLUE + "Running a Reverse IP check")
    host = urlparse(url).netloc
    
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
    try:
        result = get(lookup).text
        print(cyan+" [+]"+result)
    except:
        print(red+' Invalid IP address')


if __name__ == "__main__":
    ReverseIP()

import colorama
from colorama import Fore, Back, Style

import requests

colorama.init(autoreset=True)


def ClickJacking(url):
    print(Fore.BLUE + "Checking the URL for Clckjacking")
    try:
        res = requests.get(url)
        if not "X-Frame-Options" in res.headers:
            print(Fore.GREEN + " Website is vulnerable to ClickJacking")
    except:
        print(Fore.RED + " Website is not Vulnerable to ClickJacking")


if __name__ == "__main__":
    ClickJacking()

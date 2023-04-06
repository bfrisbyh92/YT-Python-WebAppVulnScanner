import colorama
from colorama import Fore, Back, Style

from urllib.request import urlopen

colorama.init(autoreset=True)


def ClickJacking():
    url = input(Back.BLACK + Fore.CYAN + "Enter host >> ")
    data = urlopen(url)
    headers = data.info()

    if not "X-Frame-Options" in headers:
        print(Fore.GREEN + "Website is vulnerable to ClickJacking")
    else:
        print(Fore.RED + "Website is not Vulnerable to ClickJacking")


if __name__ == "__main__":
    ClickJacking()

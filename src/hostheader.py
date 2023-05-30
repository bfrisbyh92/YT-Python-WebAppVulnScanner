import requests
from colorama import Fore, Style, Back

cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT


def HostHeader(url):
    print(Fore.BLUE + "Checking the URL for Host Header Injection")
    headers = {'Host': 'http://evil.com'}
    try:
        response = requests.get(url, headers=headers)
        if 'evil.com' in response.headers:
            print(green + " Vulnerable to Host Header Injection")
    except:
        print(Back.RED + Fore.BLACK + Style.NORMAL +
                " NOT VULNERABLE TO HOST HEADER INJECTION")


if __name__ == "__main__":
    HostHeader()

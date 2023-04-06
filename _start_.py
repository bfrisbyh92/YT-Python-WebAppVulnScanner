# Package Imports
import colorama
from colorama import Fore, Back, Style

# My Imports
from clickjack import ClickJacking
from hostheader import HostHeader
from subdomain import google_subdomains
from reverseip import ReverseIP
from xss_reflected import scan_for_xss_vulnerabilities

colorama.init(autoreset=True)

cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
red = Fore.RED + Back.BLACK + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT

banner = cyan + '''
░█████╗░██╗░░░██╗██████╗░███████╗██████╗░░██████╗░██╗░░░░░░░██╗███████╗███████╗██████╗░
██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗
██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝╚█████╗░░╚██╗████╗██╔╝█████╗░░█████╗░░██████╔╝
██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗░╚═══██╗░░████╔═████║░██╔══╝░░██╔══╝░░██╔═══╝░
╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║██████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░░░░
░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░░░░
    ❚█══❚█══✴.·´¯`·.·★█▓▒▒░░░Web App Vulnerability Scanner░░░▒▒▓█✴.·´¯`·.·★══█❚══█❚
'''
tank = cyan + '''
░░░░░░███████ ]▄▄▄▄▄▄▄▄
▂▄▅█████████▅▄▃▂
I███████████████████].
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...
'''


def Main():
    print(tank)
    print(banner)
    print(yellow+"Github profile: https://github.com/bfrisbyh92")
    print(green+"")
    print(green+"Available Modules")
    print(green+"")
    print(green+"1. ClickJacking")
    print(green+"2. Host Header Injection")
    print(green+"3. Subdomain Enumeration")
    print(green+"4. Reverse IP Lookup")
    print(green +"5. XSS Reflected")
    print(yellow+"")
    # print(yellow+"Note: Type 'help' inside any module for more information.")
    while True:
        inp = input(Fore.GREEN + Back.BLACK + "Module »»-----------► ")
        if inp == '1':
            ClickJacking()
        elif inp == '2':
            HostHeader()
        elif inp == '3':
            google_subdomains()
        elif inp == '4':
            ReverseIP()
        elif inp == '5':
            scan_for_xss_vulnerabilities()
        elif inp == 'help':
            print(green + """
               1. ClickJacking
               2. Host Header Injection
               3. Subdomain Enumeration
               4. Reverse IP Lookup
               5. XSS Reflected
               """ + Style.RESET)
        else:
            print(red + "Invalid input. Please try again." + Style.RESET)


if __name__ == "__main__":
    Main()

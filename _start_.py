# Package Imports
import colorama
from colorama import Fore, Back, Style
from urllib.parse import urlparse

# My Imports
from src.clickjack import ClickJacking
from src.hostheader import HostHeader
from src.subdomain import google_subdomains
from src.reverseip import ReverseIP
from src.xss_reflected import scan_for_xss_vulnerabilities

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
    print(tank, "\n" ,banner)
    print(green + "This tool checks for...\n\t\t1.Clickjacking\n\t\t2.Host header Injection\n\t\t3.Subdomain Enumeration\n\t\t4.Reverse IP\n\t\t5.Cross Site Scripting")
    url = input(Back.BLACK + Fore.CYAN + "\n\nEnter host >> ")
    if urlparse(url).scheme:
        ClickJacking(url)   
        HostHeader(url)   
        google_subdomains(url)  
        ReverseIP(url) 
        scan_for_xss_vulnerabilities(url) 

    else:
        print(red + " The URL is not in proper format \n [+] Example : https://www.example.com or http://www.example.com\n" )
            

if __name__ == "__main__":
    Main()

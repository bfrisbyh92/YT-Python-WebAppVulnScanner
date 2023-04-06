import requests
from urllib.parse import urlparse
from colorama import Fore, Style, Back
from bs4 import BeautifulSoup
import time

cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT


def google_subdomains():
    domain = input(Back.BLACK + Fore.CYAN + "Enter domain >> ")
    subdomains = []

    for i in range(10):
        # search Google for domain
        url = f'https://www.google.com/search?q=site%3A{domain}&num=100&start={i * 100}'

        # make request with timeout
        try:
            response = requests.get(url, timeout=2)
            response.raise_for_status()  # raise exception for non-200 status codes
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                print(yellow + "Google is rate limiting us. Try again later.")
            else:
                print(red + f"Error {e.response.status_code} occurred.")
            return

        # parse Google search results
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')

        # extract subdomains from search results
        for link in links:
            href = link.get('href')
            if href.startswith('/url?q='):
                url = urlparse(href[7:]).hostname
                if url and url.endswith('.' + domain):
                    subdomains.append(url)

        # add a short timeout between requests to avoid overloading the server
        time.sleep(0.5)

    # print subdomains
    if subdomains:
        print(green + "Subdomains found:")
        for subdomain in set(subdomains):
            print(cyan + subdomain)
    else:
        print(red + "No subdomains found.")


if __name__ == "__main__":
    google_subdomains()

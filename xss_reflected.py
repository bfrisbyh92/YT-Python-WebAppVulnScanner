import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import init, Fore, Back, Style

# Initialize Colorama for colored console output
init(autoreset=True)

def scan_for_xss_vulnerabilities():
    
    # User input for the starting URL
    start_url = input("Enter the starting URL: ")

    # Maximum depth to crawl
    max_depth = int(input("Enter the max depth you want to check: "))

    # Set of visited URLs to avoid revisiting the same page
    visited = set()

    # Stack of URLs to visit, starting with the starting URL
    to_visit = [(start_url, 0)]

    # Depth-first search algorithm to crawl forward
    while to_visit:
        url, depth = to_visit.pop()
        
        # Skip this URL if it has already been visited or exceeds the maximum depth
        if url in visited or depth > max_depth:
            continue
        
        # Make a request to the URL
        response = requests.get(url)
        
        # Add the URL to the set of visited URLs
        visited.add(url)
        
        # Check for potential XSS vulnerabilities in form fields
        soup = BeautifulSoup(response.content, "html.parser")
        forms = soup.find_all("form")
        
        for form in forms:
            fields = form.find_all("input")
            payload = "<script>alert('XSS')</script>"
            data = {}
            
            for field in fields:
                if field.get("type") in ["text", "hidden"]:
                    data[field.get("name")] = payload
            
            # Send a request with the XSS payload and check if it is reflected in the response
            xss_response = requests.post(urljoin(url, form.get("action")), data=data)
            
            if payload in xss_response.text:
                print(Fore.BLACK + Back.GREEN + f"Possible XSS vulnerability detected at {urljoin(url, form.get('action'))}!" + Style.RESET_ALL)
            else:
                print(Fore.BLACK + Back.RED + f"XSS check failed on {urljoin(url, form.get('action'))}" + Style.RESET_ALL)
        
        # Add the URL to the set of visited URLs
        visited.add(url)
    
        # Parse the HTML content of the response and find all links on the page
        links = soup.find_all("a")
    
    # Add any new links to the stack of URLs to visit
        for link in links:
            new_url = urljoin(url, link.get("href"))
            to_visit.append((new_url, depth+1))
        
    # Print a message indicating the progress of the scan
        print(Fore.BLACK + Back.YELLOW + f"{len(visited)} pages visited so far..." + Style.RESET_ALL)

if __name__ == "__main__":
    scan_for_xss_vulnerabilities()
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

class WikipediaPage:
    def __init__(self, url):
        self.url = url
        self.links = []

def extract_links(page):
    response = requests.get(page.url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/wiki/') and ':' not in href:
                page.links.append("https://en.wikipedia.org" + href)

def search_hitler_page(page, depth, max_depth):
    if depth == max_depth:
        return False
    if "Hitler" in page.url:
        print("Found Hitler page:", page.url)
        return True
    else:
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(extract_links, WikipediaPage(link)) for link in page.links]
            for future in futures:
                future.result()
                for link in future.result().links:
                    if search_hitler_page(WikipediaPage(link), depth + 1, max_depth):
                        return True
    return False

def main(start_page_url):
    start_page = WikipediaPage(start_page_url)
    if search_hitler_page(start_page, 0, 6):
        print("Path to Hitler page found.")
    else:
        print("Hitler not found.")

if __name__ == "__main__":
    start_page_url = input("Enter the URL of the Wikipedia page to start from: ")
    main(start_page_url)

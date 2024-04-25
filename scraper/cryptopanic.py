import requests
from bs4 import BeautifulSoup

def scrape_cryptopanic_titles():
    url = 'https://cryptopanic.com/news'
    headers = {
        'Accept': 'application/json',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://cryptopanic.com/',
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        print(soup)

        titles = soup.find_all('div', class_='news-title')

        scraped_titles = [title.text.strip() for title in titles]
        
        return scraped_titles
    else:
        print("Failed to retrieve data from CryptoPanic")


if __name__ == "__main__":
    titles = scrape_cryptopanic_titles()
    if titles:
        print("Scraped Titles:")
        for title in titles:
            print(title)
    else:
        print("No titles scraped.")

import requests
from bs4 import BeautifulSoup

def scrape_google_news(query, num_results):
    # Set the URL for Google News search with the query
    url = f"https://www.google.com/search?q={query}&tbm=nws&num={num_results}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5"
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the news articles in the search results
        articles = soup.find_all('div', class_='n0jPhd ynAwRc MBeuO nDgy9d')

        # Print the titles and URLs of the news articles
        for article in articles:
            title = article.text
            print(title)


scrape_google_news("Akash Network", 1000)
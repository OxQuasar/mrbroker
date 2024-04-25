import requests
from bs4 import BeautifulSoup

# Function to scrape Twitter search results
def scrape_twitter_search(query):
    url = f"https://twitter.com/search?q={query}&src=typed_query"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Mobile Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    print(response.text)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        tweets = soup.find_all("div", class_="tweet")
        for tweet in tweets:
            tweet_text = tweet.find("div", class_="tweet-text").text.strip()
            print(tweet_text)
            print("------------")
    else:
        print("Failed to fetch Twitter search results.")

# Search query
search_query = "Akash Network"

# Scrape Twitter search results
scrape_twitter_search(search_query)


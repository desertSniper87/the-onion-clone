import requests
from bs4 import BeautifulSoup
import time

class NewsScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_prothom_alo(self):
        url = "https://www.prothomalo.com/"
        return self._generic_scrape(url, ['h1', 'h2', 'h3', 'h4'], "Prothom Alo")

    def scrape_bdnews24(self):
        url = "https://bdnews24.com/"
        return self._generic_scrape(url, ['h1', 'h2', 'h3'], "bdnews24")

    def _generic_scrape(self, url, tags, source_name):
        try:
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            headlines = []
            for tag in tags:
                for item in soup.find_all(tag):
                    text = item.get_text(strip=True)
                    if text and len(text) > 20 and text not in headlines:
                        headlines.append(text)

            print(f"Successfully scraped {len(headlines)} headlines from {source_name}")
            return headlines
        except Exception as e:
            print(f"Error scraping {source_name}: {e}")
            return []

def fetch_real_news():
    scraper = NewsScraper()
    all_headlines = []
    all_headlines.extend(scraper.scrape_prothom_alo())
    # Adding more sources as needed
    return all_headlines

if __name__ == "__main__":
    news = fetch_real_news()
    print(f"\nTotal Fetched Headlines: {len(news)}")
    for i, h in enumerate(news[:10], 1):
        print(f"{i}. {h}")

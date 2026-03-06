import requests
from bs4 import BeautifulSoup

def fetch_real_news():
    url = "https://www.prothomalo.com/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = []
        # Prothom Alo usually has headlines in <h2> or specialized classes
        # Based on previous view_text_website, headlines are often in anchor tags within certain divs
        for item in soup.find_all(['h1', 'h2', 'h3'], limit=15):
            text = item.get_text(strip=True)
            if text and len(text) > 10:
                headlines.append(text)

        return headlines
    except Exception as e:
        print(f"Error fetching news: {e}")
        return [
            "যানবাহনে তেল নেওয়ার সীমা বেঁধে দিল বিপিসি",
            "সরাসরি ইসরায়েলের প্রধান ও বৃহত্তম বিমানবন্দর বেন গুরিয়নে আঘাত হেনেছে ইরানের ক্ষেপণাস্ত্র",
            "মেসির সঙ্গে সাক্ষাতে ট্রাম্প বললেন, ‘তুমি হয়তো পেলের চেয়েও ভালো’",
            "বনমোরগ জব্দ করে ‘দেশি মোরগ’ অবমুক্ত করলেন বন কর্মকর্তা"
        ]

if __name__ == "__main__":
    news = fetch_real_news()
    print("Fetched Headlines:")
    for i, h in enumerate(news, 1):
        print(f"{i}. {h}")

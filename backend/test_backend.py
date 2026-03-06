import pytest
from backend.scraper import NewsScraper
from backend.satire_engine import satirize, generate_satire_news

def test_scraper():
    scraper = NewsScraper()
    news = scraper.scrape_prothom_alo()
    assert isinstance(news, list)
    assert len(news) > 0
    assert all(isinstance(h, str) for h in news)

def test_satire_engine():
    headline = "মেসি গোল করেছেন"
    satirical = satirize(headline)
    assert isinstance(satirical, str)
    assert len(satirical) > len(headline) or "মেসি" in satirical

def test_generate_satire_news():
    headlines = ["খবর ১", "খবর ২"]
    results = generate_satire_news(headlines)
    assert len(results) == 2
    assert all(isinstance(r, str) for r in results)

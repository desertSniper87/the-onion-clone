# Algorithmic Decisions

## Scraper Algorithm
`backend/scraper.py:L4-L35` — `NewsScraper` — A class-based multi-source gathering logic for Bangla headlines. It handles site-specific tags and general extraction.

## Data Gathering & De-duplication
`backend/gather_news.py:L6-L36` — `gather_and_save` — Orchestrates multiple scrapers, removes duplicates, and maintains a JSON record of all gathered news.

## Satire Transformation Algorithm (Mock)
`backend/satire_engine.py:L3-L25` — `satirize` — Placeholder logic for transforming a real headline into a satirical version using string manipulation.

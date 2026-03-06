import json
import os
from datetime import datetime
from backend.scraper import NewsScraper

def gather_and_save():
    scraper = NewsScraper()

    # Gather from multiple sources
    data = {
        "timestamp": datetime.now().isoformat(),
        "sources": {
            "prothom_alo": scraper.scrape_prothom_alo(),
            "bdnews24": scraper.scrape_bdnews24()
        }
    }

    # Flatten headlines for unique storage
    all_headlines = []
    for source, headlines in data["sources"].items():
        all_headlines.extend(headlines)

    unique_headlines = list(set(all_headlines))
    data["all_unique_headlines"] = unique_headlines
    data["total_count"] = len(unique_headlines)

    # Save to file
    file_path = "data/raw_news.json"

    # Load existing data if available to merge
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
                # Merge logic: add new unique headlines to the history
                history = existing_data.get("history", [])
                history.append({
                    "timestamp": data["timestamp"],
                    "count": data["total_count"]
                })
                data["history"] = history
        except Exception as e:
            print(f"Error loading existing data: {e}")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Saved {data['total_count']} unique headlines to {file_path}")

if __name__ == "__main__":
    gather_and_save()

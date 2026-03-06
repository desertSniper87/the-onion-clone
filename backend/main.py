from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .scraper import fetch_real_news
from .satire_engine import generate_satire_news

app = FastAPI()

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/news")
def get_satirical_news():
    real_headlines = fetch_real_news()
    satirical_headlines = generate_satire_news(real_headlines)

    # Structure for the frontend
    stories = []
    for i, (original, satirical) in enumerate(zip(real_headlines, satirical_headlines)):
        stories.append({
            "id": i,
            "title": satirical,
            "original": original,
            "category": "ব্যঙ্গাত্মক" if i % 2 == 0 else "খবর",
            "author": "অনিয়ন বাংলা ডেস্ক"
        })

    return stories

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

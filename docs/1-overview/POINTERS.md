# Pointers & Next Steps: Bangla Satire Model Development

This guide outlines the critical actions needed to build and fine-tune your "Onion Bangla" satirical model.

---

## 1. Collect Data (The Raw Ingestion)
- **Current State:** Use `backend/gather_news.py` to scrape real news headlines from Prothom Alo and Ittefaq.
- **Action:**
    - Run the script daily: `PYTHONPATH=. python3 backend/gather_news.py`.
    - Expand to more sources (e.g., Bangla Tribune, Jugantor) by adding them to `backend/scraper.py`.
    - Goal: 5,000+ unique real-news headlines for training diversity.

## 2. Build the Dataset (The "Satirizer" Step)
Since there is no large paired dataset of Bangla satire, you must create one using a **Teacher Model**:
- **Action:**
    - Take your `data/raw_news.json`.
    - Use a high-end LLM (GPT-4o or Claude 3.5 Sonnet) with a specialized prompt to generate satirical versions of your collected real headlines.
    - Format as JSONL: `{"instruction": "Transform this news to satire", "input": "[Real News]", "output": "[Satirical News]"}`.
    - **Crucial:** Manually edit/review at least 100-200 pairs to ensure the humor is culturally relevant and hits the "Onion" style.

## 3. Fine-Tune the Model
- **Action:**
    - **Base Model:** Choose Llama 3 (8B) or TituLM-Gemma-2-2B.
    - **Infrastructure:** Use RunPod or Lambda Labs with an RTX 4090 or A100 (see `docs/1-overview/README.md` for pricing).
    - **Technique:** Use **LoRA/QLoRA** for efficient training.
    - **Prompt Format:** Use a consistent template (e.g., Alpaca or ChatML) during both training and inference.
    - **Evaluation:** Test the model on 50 headlines it has never seen before. Does it sound like "Rosh Alo"?

## 4. Deploy and Infer
- **Action:**
    - Save your LoRA adapters.
    - Integrate the fine-tuned model into `backend/satire_engine.py` (replacing the current mock logic).
    - Serve via the existing FastAPI `/api/news` endpoint to see it on your Next.js frontend.

---

## Summary Checklist
- [ ] Run scraper daily to build a massive headline pool.
- [ ] Use GPT-4o to generate 2,000 paired satire headlines.
- [ ] Rent a RunPod GPU (A100) for a few hours of LoRA fine-tuning.
- [ ] Merge adapters and update the backend engine.

import random

def satirize(headline):
    """
    Mock satirization logic for Bangla headlines.
    In a real scenario, this would call an LLM API.
    """
    # Some satirical prefixes/suffixes in Bangla for the mock
    mock_additions = [
        " (ব্রেকিং নিউজ: এটি একটি ফ্যান্টাসি!)",
        " - দাবি জিন জাতির",
        " নিয়ে চিন্তিত এলিয়েনরা",
        ": আসল ঘটনা ভিন্ন",
        " - বিশেষজ্ঞের বদলে আমজনতার মত",
        " - হাসতে হাসতে পেট ফালি",
        " (পড়ুন এবং মাথা চুলকান)"
    ]

    # Simple rule-based mock transformation
    if "ট্রাম্প" in headline:
        return f"ডোনাল্ড ট্রাম্পের বাংলা ভাষা শিক্ষার নতুন মিশন: {headline}"
    elif "মেসি" in headline:
        return f"মেসির বদলে এবার মাঠে নামছেন হিরো আলম: {headline}"
    elif "তেল" in headline:
        return f"তেলের বদলে পানি দিয়ে গাড়ি চালানোর ফর্মুলা আবিষ্কার: {headline}"

    return headline + random.choice(mock_additions)

def generate_satire_news(headlines):
    return [satirize(h) for h in headlines]

if __name__ == "__main__":
    sample_headlines = [
        "যানবাহনে তেল নেওয়ার সীমা বেঁধে দিল বিপিসি",
        "মেসির সঙ্গে সাক্ষাতে ট্রাম্প বললেন",
        "ঢাকা মেডিকেলের বার্ন ইউনিটের নার্সের লাশ উদ্ধার"
    ]
    satirical_news = generate_satire_news(sample_headlines)
    for original, satirical in zip(sample_headlines, satirical_news):
        print(f"Original: {original}")
        print(f"Satirical: {satirical}\n")

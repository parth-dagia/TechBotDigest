import feedparser
from hf_summarize import summarize_text  # Your summarizer function
from telegram_sender import send_message_to_telegram  # Your Telegram bot sender
import re

rss_feeds = [
    "https://www.technologyreview.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "https://www.reddit.com/r/technology/.rss"
]

def escape_markdown(text):
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

def fetch_articles():
    articles = []

    for url in rss_feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:  # Top 3 articles per feed
            article = {
                "title": entry.title,
                "link": entry.link,
                "summary": entry.get("summary", "No summary available.")
            }
            articles.append(article)

    return articles

if __name__ == "__main__":
    articles = fetch_articles()

    full_message = "🧠 *Daily Tech Digest*\n\n"

    for article in articles:
        print(f"🔍 Processing: {article['title']}")
        summary = summarize_text(article['summary'])

        title = escape_markdown(article['title'])
        summary = escape_markdown(summary)
        link = article['link']  # URLs don't need escaping

        full_message += f"🔹 *{title}*\n"
        full_message += f"{summary}\n"
        full_message += f"🔗 [Read More]({link})\n\n"

    full_message += "---\n"
    full_message += f"_Total articles: {len(articles)}_"

    if len(full_message) > 4000:
        full_message = full_message[:3900] + "\n\n⚠️ Message truncated..."

    print("📤 Sending to Telegram...")
    send_message_to_telegram(full_message)

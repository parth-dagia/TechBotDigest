# TechBotDigest
# 📰 Tech News Summarizer  

Stay updated with the latest in technology without information overload!  
This Python script automatically fetches the **top 5 tech news stories** from trusted sources, summarizes them into concise snippets, and delivers them to you daily.  

---

## ✨ Features  
- Fetches **top 5 tech stories** every day  
- Summarizes articles into short, easy-to-digest snippets  
- Automated with a **cron job** (runs daily at 10 PM on Ubuntu)  
- No manual browsing, no endless scrolling — just the right amount of information  

---

## 📡 Sources  
The script collects updates from:  
- [MIT Technology Review](https://www.technologyreview.com/feed/)  
- [The Verge](https://www.theverge.com/rss/index.xml)  
- [Reddit r/Technology](https://www.reddit.com/r/technology/.rss)  

---

## ⚙️ Installation & Setup  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/USERNAME/tech-news-summarizer.git
   cd tech-news-summarizer
2.
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3.
pip install -r requirements.txt
4.
python main.py


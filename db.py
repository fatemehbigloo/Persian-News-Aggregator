
import sqlite3
import requests
from bs4 import BeautifulSoup

DATABASE = "news.db"
BASE_URL = "https://www.varzesh3.com"
URL_PAGE = "https://www.varzesh3.com"


# ---------- اتصال به دیتابیس ----------
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# ---------- ایجاد جدول در صورت نیاز ----------
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            link TEXT
        )
    """)
    conn.commit()
    conn.close()


# ---------- گرفتن خبر از سایت ----------
def fetch_news_from_site(limit: int = 200):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(URL_PAGE, headers=headers, timeout=20)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    news_list = []

    for a in soup.select('a[href*="/news/"]'):
        href = a.get("href")
        if not href:
            continue

        spans = a.find_all("span", recursive=False)
        title = ""
        if len(spans) >= 2:
            title = spans[1].get_text(strip=True)
        else:
            span_texts = [s.get_text(strip=True) for s in a.find_all("span")]
            title = next((t for t in span_texts if t), "").strip()
            if not title:
                title = a.get_text(strip=True)

        if not title:
            continue

        link = href if href.startswith("http") else BASE_URL + href
        news_list.append({"title": title, "link": link})

        if len(news_list) >= limit:
            break

    return news_list


# ---------- ذخیره خبرها در دیتابیس ----------
def save_news_to_db(news_list):
    conn = get_db()
    cursor = conn.cursor()

    for item in news_list:
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO news (title, link) VALUES (?, ?)",
                (item["title"], item["link"])
            )
        except Exception as e:
            print("خطا در ذخیره:", e)

    conn.commit()
    conn.close()


# ---------- جستجو در دیتابیس ----------
def search_news_in_db(keyword: str):
    if not keyword:
        return []

    conn = get_db()
    keyword_pattern = f"%{keyword}%"
    rows = conn.execute(
        "SELECT id, title, link FROM news WHERE title LIKE ? ORDER BY id DESC",
        (keyword_pattern,)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


# ---------- نمایش همه خبرها ----------
def get_all_news(limit: int = 50):
    conn = get_db()
    rows = conn.execute(
        "SELECT id, title, link FROM news ORDER BY id DESC LIMIT ?",
        (limit,)).fetchall()
    conn.close()
    return [dict(row) for row in rows]


# ---------- همگام‌سازی دیتابیس با سایت ----------
def sync_news():
    news_list = fetch_news_from_site()
    save_news_to_db(news_list)

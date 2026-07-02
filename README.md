# Persian-News-Aggregator
**run app.py for see exit**
 simple web application with **Flask** that receives, stores and displays the news of the day from various sources. Users can browse the news or search by keyword.

📄 README - Persian News Aggregator

markdown
# 📰 Persian News Aggregator

A simple web application with **Flask** that receives, stores and displays the news of the day from various sources. Users can browse the news or search by keyword.

## 🎯 Usage
- **Automatically collect news** from specified sources (via `sync_news` function)
- **Storage in database** (SQLite)
- **Show news list** on the home page
- **Search news** by keyword

## 📋 Prerequisites
- Python 3.8 or higher
- Internet connection (to receive news)

🚀 How to run
1. Clone the project or download the files.
2. In the terminal, enter the project folder:
bash
cd news-aggregator
3. Run the program:
bash
python app.py
4. Open in the browser:
http://127.0.0.1:5000

📝 File Descriptions
app.py - Paths (Paths)
Path Description
/Home - Show the last 50 news
/search Page Search - News Search Form
/results Search Results - Show news related to the keyword

⚠️ Important Notes
· Database is automatically created on first run
· The sync_news function must be run before displaying news (currently it is done at runtime)
· If the news source is offline, the program will not throw an error and will use the existing news
· To automatically update news, you can use cronjob or Task Scheduler

👨‍💻 Developer
[fatemeh bigloo] - [ghasembigloo@gmail.com]

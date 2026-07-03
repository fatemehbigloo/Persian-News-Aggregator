# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from db import  init_db, sync_news, get_all_news, search_news_in_db

app = Flask(__name__)


# ---------- صفحه اصلی ----------
@app.route("/")
def index():
    news = get_all_news(50)
    return render_template("index.html", news=news)


# ---------- صفحه جستجو ----------
@app.route("/search")
def search_page():
    q = request.args.get("q", "")
    return render_template("search.html", q=q)


# ---------- صفحه نتایج جستجو ----------
@app.route("/results")
def search_results():
    q = request.args.get("q", "").strip()
    news = search_news_in_db(q)
    return render_template("results.html", news=news, q=q)
        # در فایل app.py


init_db()
sync_news()
if __name__ == '__main__':
    app.run()

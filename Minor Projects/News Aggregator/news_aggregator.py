"""
News Aggregator
Fetches and displays the latest news headlines using the NewsAPI.

Setup:
    1. Get a free API key from https://newsapi.org/
    2. Set it as an environment variable named 'NEWSAPI_KEY',
       OR replace the placeholder below directly.
    3. Install dependency: pip install requests

Usage:
    python news_aggregator.py
"""

import os
import requests

API_KEY = os.getenv("NEWSAPI_KEY", "a19db6917a494368ae1e12e5f5660f42")
BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_news(country="us", category=None, query=None, page_size=10):
    params = {
        "apiKey": API_KEY,
        "country": country,
        "pageSize": page_size,
    }
    if category:
        params["category"] = category
    if query:
        params["q"] = query

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None


def display_articles(data):
    if not data or data.get("status") != "ok":
        print("Could not retrieve news. Check your API key and internet connection.")
        return

    articles = data.get("articles", [])
    if not articles:
        print("No articles found for the given criteria.")
        return

    print(f"\nFound {len(articles)} articles:\n")
    for i, article in enumerate(articles, start=1):
        print(f"{i}. {article.get('title')}")
        print(f"   Source: {article.get('source', {}).get('name')}")
        print(f"   Published: {article.get('publishedAt')}")
        print(f"   URL: {article.get('url')}\n")


def main():
    print("=== News Aggregator ===")

    if API_KEY == "YOUR_API_KEY_HERE":
        print("Warning: You must set your NewsAPI key before running this script.")
        print("Get a free key at https://newsapi.org/\n")

    country = input("Enter country code (default 'us'): ").strip() or "us"
    category = input(
        "Enter category (business, entertainment, general, health, "
        "science, sports, technology) or press Enter to skip: "
    ).strip() or None
    query = input("Enter a search keyword (optional): ").strip() or None

    data = fetch_news(country=country, category=category, query=query)
    display_articles(data)


if __name__ == "__main__":
    main()

"""Scrape article titles and links from the economic news section of Tasnim News Agency."""

import csv
import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.tasnimnews.com"
SECTION_URL = (
    BASE_URL
    + "/fa/service/77/%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86"
)
ARTICLE_SELECTOR = (
    "section.news-container.top-news-service > section.content > article.list-item"
)
OUTPUT_FILE = "data.csv"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; news-scraper/1.0; educational project)"}
TIMEOUT = 15  # seconds


def fetch_page(url):
    """Download the page and return its raw bytes. Raises requests.RequestException on failure."""
    response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()
    return response.content


def parse_articles(html_content):
    """Return a list of [title, full_link] pairs found in the section page."""
    soup = BeautifulSoup(html_content, "html.parser")
    articles = []
    for item in soup.select(ARTICLE_SELECTOR):
        title_tag = item.select_one("h2")
        link_tag = item.select_one("a[href]")
        if title_tag is None or link_tag is None:
            continue  # skip items that do not have the expected structure
        articles.append([title_tag.text.strip(), urljoin(BASE_URL, link_tag["href"])])
    return articles


def save_csv(articles, path=OUTPUT_FILE):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["News title", "News link"])
        writer.writerows(articles)


def main():
    try:
        html_content = fetch_page(SECTION_URL)
    except requests.RequestException as error:
        sys.exit(f"Could not fetch the page: {error}")

    articles = parse_articles(html_content)
    if not articles:
        sys.exit(
            "No articles found. The page structure may have changed; "
            f"the existing {OUTPUT_FILE} was left untouched."
        )

    save_csv(articles)
    print(f"Saved {len(articles)} articles to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

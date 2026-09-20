# 📰 Tasnim News Scraper

A Python script for automatic extraction of news titles and links from the economic news section of Tasnim News Agency website.

---

## 📋 Project Description

This project uses `requests` and `BeautifulSoup` to process the economics section of the Tasnim website and extract the title and full link of each article.

---

## ⚙️ Prerequisites

Before running, install the required libraries:

```bash
pip install requests beautifulsoup4
```

---

## 🚀 How to Run

```bash
python main.py
```

After execution, the `data.csv` file will be created in the same directory.

---

## 📁 Output

The `data.csv` file contains two columns:

| News title | News link |
|-----------|----------|
| Article title | https://www.tasnimnews.com/... |

**Example:**
```
News title,News link
Dollar exchange rate increase,https://www.tasnimnews.com/fa/news/...
Stock market improved,https://www.tasnimnews.com/fa/news/...
```

---

## 🔗 Data Source

- **Website:** [Tasnim News Agency](https://www.tasnimnews.com)
- **Section:** [Iran Economy News](https://www.tasnimnews.com/fa/service/77/%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86)

---

## 📂 Project Structure

```
news-scraper/
│
├── main.py          # Main script
├── data.csv         # Output (created after running)
├── README.md        # This file
└── LICENSE          # MIT License
```

---

## 🔍 How It Works

The script performs the following steps:

1. **Fetch Page:** Downloads the economic news page using `requests`
2. **Parse HTML:** Searches for article elements using `BeautifulSoup`
3. **Extract Information:** Extracts the title (h2) and link (href) of each article
4. **Save to CSV:** Saves the data in `data.csv` file with UTF-8 encoding

---

## 📝 Important Notes

- ⚠️ **File Overwrite:** Each time the script runs, it completely overwrites the CSV file (previous data is deleted)
- 🔄 **Website Changes:** If the HTML structure of Tasnim website changes, CSS selectors used may need to be updated
- 🌐 **Encoding:** The output file is saved with UTF-8 encoding
- 📡 **User-Agent and timeout:** Requests are sent with a User-Agent header and a 15-second timeout
- ⚖️ **Responsible use:** Respect the website's terms of service and `robots.txt`. This project is for educational purposes

---

## 📜 License

This project is published under the MIT License. For more information, refer to the [LICENSE](LICENSE) file.

---

## 💡 Suggestions for Improvement

- Add news publication date
- Implement timestamped storage to prevent data loss
- Add delay between requests (Rate Limiting)
- Support for multiple pages

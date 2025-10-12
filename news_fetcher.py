import requests

class NewsFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/everything"

    def fetch_news(self, keyword, top_n=3):
        params = {
            "q": keyword,
            "apiKey": self.api_key,
            "pageSize": top_n,
            "sortBy": "publishedAt",
            "language": "en"
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            articles = data.get("articles", [])
            return [{"title": a["title"], "url": a["url"]} for a in articles[:top_n]]
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return []

if __name__ == "__main__":
    api_key = os.getenv("API_KEY")   # Replace with your API key
    fetcher = NewsFetcher(api_key)

    print("Welcome to News Fetcher!")
    print("Type: show news about <keyword> OR exit to quit\n")

    while True:
        command = input("Enter command: ").strip()
        if command.lower() == "exit":
            print("Exiting. Goodbye!")
            break
        elif command.lower().startswith("show news about"):
            keyword = command[16:].strip()
            news_list = fetcher.fetch_news(keyword)
            if news_list:
                print(f"\nTop {len(news_list)} news for '{keyword}':\n")
                for i, article in enumerate(news_list, start=1):
                    print(f"{i}. {article['title']}")
                    print(f"   URL: {article['url']}\n")
            else:
                print("No news found or network error occurred.")
        else:
            print("Invalid command. Use: show news about <keyword> or exit")

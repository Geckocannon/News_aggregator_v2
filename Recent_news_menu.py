def Recent_news_menu():
    print("\nFetching todays news from each outlet...\n")
    todays_news = []

    outlet_urls [ 
        "https://feeds.feedburner.com/TheHackersNews",
        "https://research.checkpoint.com/feed",
        "https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v",
        "https://www.bleepingcomputer.com/feed/",
        "https://krebsonsecurity.com/feed"
    ]

    for url in outlet_urls:
        articles = fetch(url=url, days=1)
        todays_news.extend(articles)

    if todays_news:
        with open("fetched.json", "w", encoding="utf-8") as f:
            json.dump(todays_news, f, indent=4)

    while True:
        display(articles)
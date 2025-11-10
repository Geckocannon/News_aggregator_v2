def Recent_news_menu():
    print("\nFetching todays news from each outlet...\n")
    while true:
        todays_news = []
        thn = fetch(url="https://feeds.feedburner.com/TheHackersNews", days=1).append(todays_news)
        cr = fetch(url="https://research.checkpoint.com/feed", days=1).append(todays_news)
        gti = fetch(url="https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v", days=1).append(todays_news)
        bc = fetch(url="https://www.bleepingcomputer.com/feed/", days=1).append(todays_news)
        kos = fetch(url="https://krebsonsecurity.com/feed", days=1).append(todays_news)
        display(todays_news)
    
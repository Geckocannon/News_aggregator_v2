import feedparser
import requests
import requests_cache
import time
from datetime import datetime, timedelta, UTC, timezone
from All_Functions import mashthis
import json

def fetch(url, days=3, cache_name="cache", cache_expire=600, timeout=10):


    """
    Here we basically have our get_requests function from V1. We install a cache that lasts 10 minutes. We http request the hardcoded url this time.
    Hardcoded because these are menu options not arguments being passed at the CLI. We then instantiate some fucking time rules. NGL I pulled this 
    striaght from chat GPT. It makes almost 0 sense to me, except that it takes some cutoff which is the time now minus 3 days. It then loops
    through the entries to see if they have the attribute "published_parsed" and if they do published parsed is equal to some time thingy. If not no idea what
    the elif statement there is doing

    next up if published time is true and it is greater than or equal to the cutoff get the details and append them to recent articles. return recent 
    articles which is a list of dictionaries. Should be from the last 3 days.

    """
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://research.checkpoint.com/",
    "Connection": "keep-alive",
}

    requests_cache.install_cache(cache_name, expire_after=cache_expire)
    try:
        response = requests.get(url, timeout=timeout, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching feed: {e}")
        return[]
    
    feed = feedparser.parse(response.content)
        

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    recent_articles = []

    for entry in feed.entries:
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            published_time = datetime.fromtimestamp(time.mktime(entry.published_parsed), tz=timezone.utc)
        elif "updated_parsed" in entry and entry.updated_parsed:
            published_time = datetime.fromtimestamp(time.mktime(entry.updated_parsed), tz=timezone.utc)

        if published_time and published_time >= cutoff:
            title = entry.get("title", "No title found")
            link = entry.get("link", "No link found")
            recent_articles.append({
                "ID": mashthis(title, link),
                "title": title,
                "summary": entry.get("summary", "No summary found"),
                "link": link,
                "published": published_time.strftime("%d-%m-%y %H:%M:%S")
            })

    json_recent = json.dumps(recent_articles, indent=4)  
    with open("fetched.json", "w") as f:
        f.write(json_recent)
              
    return recent_articles





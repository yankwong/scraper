import requests


def scrape() -> bytes:
    url = "https://gamepress.gg/grandorder/servant-tier-list"
    tier_list_html = requests.get(url)
    return tier_list_html.content

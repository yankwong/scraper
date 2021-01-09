import json
from bs4 import BeautifulSoup

rarity_translator = {
    1: '★',
    2: '★★',
    3: '★★★',
    4: '★★★★',
    5: '★★★★★',
}

def get_page_json(page_content: str):
    return BeautifulSoup(page_content, 'html.parser')


def get_total_rarity(tier_list_json, target_rarity) -> int:
    all_rarities = tier_list_json.find_all('span', class_='star-rarity')
    total = 0

    for rarity in all_rarities:
        if rarity.text == rarity_translator[target_rarity]:
            total += 1

    return total

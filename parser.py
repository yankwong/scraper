import json
from bs4 import BeautifulSoup


def get_page_json(page_content: str):
    return BeautifulSoup(page_content, 'html.parser')


def get_total_rarity(tier_list_json) -> int:
    return 1

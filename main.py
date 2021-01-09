# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import pprint

# parse gamepress, generate a report to say how many servants are in each star category
# how many AOE
# how many ST
# how many support

import scraper
import parser

# generate a JSON object while u loop through the page

fgo_na_tier_list = parser.get_page_json(scraper.scrape())
one_star_total = parser.get_total_rarity(fgo_na_tier_list, 1)

if __name__ == '__main__':
    print(f'there are {one_star_total} one star servants in NA')

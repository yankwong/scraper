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
from datetime import date

today = date.today()

fgo_na_tier_list = parser.get_page_json(scraper.scrape())
one_star_total = parser.get_total_rarity(fgo_na_tier_list, 1)
two_star_total = parser.get_total_rarity(fgo_na_tier_list, 2)
three_star_total = parser.get_total_rarity(fgo_na_tier_list, 3)
four_star_total = parser.get_total_rarity(fgo_na_tier_list, 4)
five_star_total = parser.get_total_rarity(fgo_na_tier_list, 5)

total_servants = one_star_total + two_star_total + three_star_total + four_star_total + five_star_total

if __name__ == '__main__':
    print(f'As of {today} there are {total_servants} servants in FGO NA')
    print('-------------------')
    print(f'{one_star_total} of them are one star')
    print(f'{two_star_total} of them are two stars')
    print(f'{three_star_total} of them are three stars')
    print(f'{four_star_total} of them are four stars')
    print(f'{five_star_total} of them are five stars')

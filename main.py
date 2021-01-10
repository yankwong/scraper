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

total_support = parser.get_servant_type(fgo_na_tier_list, 'SUPPORT')
total_aoe = parser.get_servant_type(fgo_na_tier_list, 'AOE')
total_st = parser.get_servant_type(fgo_na_tier_list, 'ST')

total_servants = one_star_total + two_star_total + three_star_total + four_star_total + five_star_total

if __name__ == '__main__':
    print(f'As of {today} there are {total_servants} servants in FGO NA')
    print('-------------------')
    print(f'{one_star_total} of them are one star')
    print(f'{two_star_total} of them are two stars')
    print(f'{three_star_total} of them are three stars')
    print(f'{four_star_total} of them are four stars')
    print(f'{five_star_total} of them are five stars')
    print('-------------------')
    print(f'{total_st} of them are SINGLE TARGET servant')
    print(f'{total_aoe} of them are AOE servant')
    print(f'{total_support} of them are SUPPORT servant')


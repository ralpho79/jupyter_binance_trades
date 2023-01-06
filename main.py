import pairs as pa
import triangles as tr
import csvfile as csv
import profits as pr
from os import scandir
from datetime import datetime


def get_file_info(name):
    dir_entries = scandir('./')
    for entry in dir_entries:
        if entry.is_file() and entry.name==name:
            info = entry.stat()
    return info.st_mtime


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


# Check last update time for 'my_pairs.csv', 'my_triangles.csv' and 'my_profits.csv'

print('**************************************')
print(f'my_pairs.csv\t\t was last modified: {convert_date(get_file_info("my_pairs.csv"))}')
print(f'my_triangles.csv\t was last modified: {convert_date(get_file_info("my_triangles.csv"))}')
print(f'my_profits.csv\t\t was last modified: {convert_date(get_file_info("my_profits.csv"))}')


# Interface - are updates needed?

choice = input("\nDo you want to update my_pairs (~21 mins!) y/n ?")
if choice=="y": pa.load_pairs(); pa.update_pairs()

choice = input("\nDo you want to update my_triangles (~4 mins!) y/n ?")
if choice=="y": tr.find_triangles()


print("\nBest potential trades")
print("**********************************")

all_profits = pr.find_profits()
buy_buy_sell = pr.sort_profits(all_profits, 6)
buy_sell_sell = pr.sort_profits(all_profits, 11)

print("\nTop 5 for Buy-Buy-Sell")
for i in range(5):
    print(buy_buy_sell[i])

print("\nTop 5 for Buy-Sell-Sell")
for i in range(5):
    print(buy_sell_sell[i])
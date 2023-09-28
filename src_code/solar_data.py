# %%
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTTextBoxHorizontal, LTTextLineHorizontal

from utils import LineContainerList, turn_into_text
from pprint import pprint
from decimal import Decimal, InvalidOperation
from statistics import mean
from datetime import date
import pandas as pd


def extract(filename) -> list:
    """Extract Transactions from file"""
    raw_text_lines = []
    # for filepth in filenames:
    for page in extract_pages(filename):
        line_containers = LineContainerList()
        for index, container in enumerate(page):
            if isinstance(container, LTTextContainer):
                for thing in container:
                    # print(thing)
                    line_containers.add(thing)

        raw_text_lines.extend([turn_into_text(line_container) for line_container in line_containers])
        return raw_text_lines


    # txns = [self.create_txn_from(text) for text in raw_text_lines]
    # txns = list(filter(lambda x:x, txns)) # remove null values
    # if start_date:
    #     txns = list(filter(lambda x: x.date >= start_date, txns))
    # if end_date:
    #     txns = list(filter(lambda x: x.date <= end_date, txns))
    # txns.sort(key=lambda x: (x.date))
    # return txns


# %%
import os
files = os.listdir('data')
# print(files)
filename = 'data/solar_daily_2022.pdf'
assert os.path.exists(filename)


result = extract(filename)
month = 0
result = result[10:]

data = {}

for index, column in enumerate(result):
    if len(column) >=28:
        column = list(filter(lambda x: x, column.split('\n')))
        try:
            column = list(map(lambda x: Decimal(x.replace(',', '').replace(' ', '').replace(' ', '')), column))
        except InvalidOperation:
            # print(column)
            continue
        print(mean(column))
        column_index = chr(ord('a') + month)
        print('Index', column_index)
        data[column_index] = column
        month +=1
        # print(column[0])
        # print(column[-1])
        # print(len(column))
        # data = 
        print()

# print(data)
months_alpha_to_num_indices = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'l': 11,
    'k': 12,
    }

data = {
    months_alpha_to_num_indices[key]: data for key,data in data.items()
}

value_data = []
date_data = []

for month, data in data.items():
    date_data += [date(2022, month, day) for day in range(1, len(data)+1)]
    value_data += data


assert len(value_data) == len(date_data)
df = pd.DataFrame({'date': date_data, 'value': value_data})
df.to_csv('data/solar_daily_2022.csv', index=False)
df



# %%
chr(ord('a') + 1)

    
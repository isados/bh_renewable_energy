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
    for page in extract_pages(filename):
        line_containers = LineContainerList()
        for txt_box in page:
            if isinstance(txt_box, LTTextBoxHorizontal):
                for line in txt_box:
                    if isinstance(line, LTTextLineHorizontal):
                        line_containers.add(line)
    return line_containers


import os
files = os.listdir('data')
# print(files)
filename = 'data/wind_daily_2022.pdf'
assert os.path.exists(filename)


pd.DataFrame(data=turn_into_text(extract(filename))).to_csv('out.csv', index=False)

# month = 0
# result = result[10:]

# data = {}

# for index, column in enumerate(result):
#     if len(column) >=28:
#         column = list(filter(lambda x: x, column.split('\n')))
#         try:
#             column = list(map(lambda x: Decimal(x.replace(',', '').replace(' ', '').replace(' ', '')), column))
#         except InvalidOperation:
#             # print(column)
#             continue
#         print(mean(column))
#         column_index = chr(ord('a') + month)
#         print('Index', column_index)
#         data[column_index] = column
#         month +=1
#         # print(column[0])
#         # print(column[-1])
#         # print(len(column))
#         # data = 
#         print()

# # print(data)
# months_alpha_to_num_indices = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
#     'f': 6,
#     'g': 7,
#     'h': 8,
#     'i': 9,
#     'j': 10,
#     'l': 11,
#     'k': 12,
#     }

# data = {
#     months_alpha_to_num_indices[key]: data for key,data in data.items()
# }

# value_data = []
# date_data = []

# for month, data in data.items():
#     date_data += [date(2022, month, day) for day in range(1, len(data)+1)]
#     value_data += data


# assert len(value_data) == len(date_data)
# df = pd.DataFrame({'date': date_data, 'value': value_data})
# df.to_csv('data/solar_daily_2022.csv', index=False)
# df



# # %%
# chr(ord('a') + 1)

    
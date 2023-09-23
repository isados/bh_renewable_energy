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


# pd.DataFrame(data=turn_into_text(extract(filename))).to_csv('out.csv', index=False)

# %%
import numpy as np
df = pd.read_csv('data/wind_daily_2022_intermediate.csv', na_values='')
wind = df.melt(['Day'], var_name='month').replace(np.NaN, None).dropna()
wind['date'] = wind.apply(lambda x: date(2022, int(x['month']), x['Day']), axis=1)
wind = wind[['date', 'value']]
wind.to_csv('data/wind_daily_2022.csv', index=False)
wind


# %%

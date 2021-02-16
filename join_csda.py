#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Structure downloaded CVVM Naše Společnost data and join them together.
"""


import pandas as pd
import re
import os

files = os.listdir("csda/csv")
files

years = {}

for i, file in enumerate(files):
    print(i, "/", len(files), "-- ", file)
    year = re.search("(?<=V)\d\d", file).group()
    df1 = pd.read_csv("csda/csv/{}".format(file), encoding="cp1250")
    df1["file_name"] = file
    
    if not year in years:
        years[year] = []
    years[year].append(df1)

for year, dfs in years.items():
    print(year)
    df = pd.concat(dfs)
    print("joined")
    df.to_csv("csda/joined/cvvm_{}.csv".format(year), encoding="utf8")
    print("saved")


files = os.listdir("csda/joined")
files.sort()
files

dfs = []
for file in files:
    print(file)
    df = pd.read_csv("csda/joined/{}".format(file), index_col = 0)
    df["file_name_year"] = file
    dfs.append(df)
    
#df = pd.concat(dfs)

rows = []
for df in dfs:
    row = {column.lower(): True for column in df.columns}
    row["year"] = df.file_name_year.values[0]
    rows.append(row)
    
columns = pd.DataFrame(rows)
columns.year = columns.year.apply(lambda x: re.sub("(cvvm_)|(\.csv)", "", x))
columns.set_index("year", inplace=True)
columns
columns.sum().sort_values(ascending=False)

columns.sum().sort_values(ascending=False).to_frame().to_excel("test.xlsx")

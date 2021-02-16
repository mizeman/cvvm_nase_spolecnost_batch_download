#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Get an overview of which columns are available in the whole CVVM Naše
Společnost history.

Findings are used for determining which variables are usable for multi-year
statistical analysis.
"""

import pandas as pd
import re

def clean_col_name(x):
    return x.lower().replace(".", "")

files = os.listdir("csda/csv")
len(files)

files_cvvm = [file for file in files if (re.search("V[01]", file) and not re.search("V0[01]", file))]
len(files_cvvm)

files = files_cvvm

years = {}

for i, file in enumerate(files):
    print(i, "/", len(files), "-- ", file)
    year = re.search("(?<=V)\d\d", file).group()
    df1 = pd.read_csv("csda/csv/{}".format(file), encoding="cp1250")
    df1["file_name"] = file

    if not year in years:
        years[year] = []
    years[year].append(df1)

rows = []
for year, dfs in years.items():
    print(year)
    for df in dfs:
        row = {clean_col_name(column): 1 for column in df.columns}
        row["year"] = year
        row["month"] = df.file_name.values[0]
        rows.append(row)
columns = pd.DataFrame(rows)
columns.year = columns.year.apply(lambda x: re.sub("(cvvm_)|(\.csv)", "", x))
columns.month = columns.month.apply(lambda x: re.sub("(V)|(\.csv)|(_F1)", "", x))
columns.month = columns.month.apply(lambda x: re.sub("(a)|(b)|(c)|(d)|(e)", "", x))
columns.month = columns.month.apply(int)

columns.set_index("month", inplace=True)
columns
top = columns.sum().sort_values(ascending=False)
top_columns = list(top.loc[top>=10].index)
top_columns.remove("year")

columns.fillna(0, inplace=True)
columns
col_year = columns.groupby("year").mean()

col_year[top_columns].to_excel("columns_in_years.xlsx")

missing_years_in_cols = (col_year[top_columns]==0).sum(axis=0)
col_year[missing_years_in_cols.loc[missing_years_in_cols<=2].index].to_excel("columns_in_years.xlsx")

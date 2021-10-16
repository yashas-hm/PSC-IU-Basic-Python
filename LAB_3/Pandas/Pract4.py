# Download file name: winemag-data-130k-v2.csv and perform the following.
#     1) Display row number 25
#     2) Display column number 13
#     3) Display rows where country name = France
#     4) Display records where province=Michigan and taster_name=Alexander Peartree
#     5) Explore describe() for the generated dataframe.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import pandas as pd
import matplotlib as plt


def q1(data):
    print(data.loc[[25]])


def q2(data):
    print(data.iloc[:, 13])


def q3(data):
    print(data.loc[data['country'] == 'France'])


def q4(data):
    print(data.loc[(data['province'] == 'Michigan') & (data['taster_name'] == 'Alexander Peartree')])


def q5(data):
    print(data.describe())


if __name__ == '__main__':
    data = pd.read_csv('winemag-data-130k-v2.csv')
    print(data.head())
    q1(data)
    q2(data)
    q3(data)
    q4(data)
    q5(data)
    print(data.describe())

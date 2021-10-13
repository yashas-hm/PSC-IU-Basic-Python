# Create a dataframe fruit_sales that matches the diagram below:
#                 Apples          Bananas
# 2017 Sales      35              21
# 2018 Sales      41              34
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame({
        'Apples': [25, 21],
        'Bananas': [41, 34]
    },
        index=['2017 Sales', '2018 Sales'])

    print(df)


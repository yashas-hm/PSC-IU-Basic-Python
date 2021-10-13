# Create a DataFrame fruits that looks like this:
#     Apples  Bananas
#  0    30      21
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import pandas as pd


if __name__ == '__main__':
    df = pd.DataFrame({
        'Apples': [30],
        'Bananas': [21]
    })
    print(df)
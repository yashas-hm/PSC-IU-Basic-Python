# Create a variable ingredients with a Series that looks like:
#     Flour 4 cups
#     Milk 1 cup
#     Eggs 2 large
#     Spam 1 can
#     Name: Dinner, dtype: object
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import pandas as pd

if __name__ == '__main__':
    series = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner',
                       dtype=object)
    print(series)

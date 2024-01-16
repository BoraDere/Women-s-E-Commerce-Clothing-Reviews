import pandas as pd

data = pd.read_csv('Womens Clothing E-Commerce Reviews.csv')
data = pd.DataFrame(data)

a = data['Review Text']
a = a.dropna()

with open('a.txt', 'a') as f:
    for i in a:
        f.write(str(i))

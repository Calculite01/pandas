import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_csv('MOCK_DATA.csv')
df['date'] = pd.to_datetime(df['date'])

df['month'] = df['date'].dt.month
df['month'] = df['date'].dt.strftime('%b')
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

df = df.value_counts(['month','genre']).unstack()

print(df)
myplot = df.plot.bar(rot=0)
plt.xlabel("Month")
plt.ylabel("Books Borrowed")
plt.title("Books Borrowed Each Month")
plt.savefig('barchart3.png')
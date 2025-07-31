import pandas as pd
df = pd.read_csv('bookdata.csv')

# print("All book data")
# print(df)

# print("All stock")
# df = df['stock'].sum()
# print(df)

# print("Total stock of each author")
# df = df[['authorname','stock']].groupby(['authorname']).sum()
# print(df)

# print("Total stock of each genre")
# df = df[['genre','stock']].groupby(['genre']).sum()
# print(df)

# print("Number of books by each author")
# df = df['authorname'].value_counts()
# print(df)

# print("Number of books by each genre")
# df = df['genre'].value_counts()
# print(df)

# author = 'Jane Austen'
# print(f"All books by author: {author}")
# df = df.loc[df['authorname'] == author].drop(['bookid','authorname','stock'],axis='columns')
# print(df)

# genre = 'Classic'
# print(f"All books by genre: {genre}")
# df = df.loc[df['genre'] == genre].drop(['bookid','genre','stock'],axis='columns')
# print(df)




#Uncomment out to check

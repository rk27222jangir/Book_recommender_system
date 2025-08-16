import numpy as np
import pandas as pd

 
pivot_table = pd.read_pickle("movies.pkl")
similarity_score= np.load("similarity_score.npy")

books= pd.read_csv('Books.csv')
books['Book-Author']= books['Book-Author'].fillna('Unknown')
books['Publisher']= books['Publisher'].fillna('Unknown')

# Clean year data
books['Year-Of-Publication'] = pd.to_numeric(books['Year-Of-Publication'], errors='coerce')
books = books.dropna(subset=['Year-Of-Publication'])
books = books[books['Year-Of-Publication'] > 1900]  # Remove unrealistic years

def recommend(book_name):
  index= np.where(pivot_table.index==book_name)[0][0]
  similar_items= sorted(list(enumerate(similarity_score[index])), key=lambda x:x[1], reverse=True)[1:6]
  data=[]
  for i in similar_items:
    item= []
    temp_df= books[books['Book-Title']==pivot_table.index[i[0]]]
    item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
    item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
    item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
    data.append(item)
  return data


print(recommend('1984'))
print(recommend('The Da Vinci Code'))


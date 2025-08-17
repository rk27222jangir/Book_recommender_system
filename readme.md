# 🎬 Book Recommendation System  
Hello, I'm Rohit Jangir. In this project, I have created two book recommendation systems based on the **Collaborative filtering** and **Popularity filtering** based techniques.  


## 📂 Dataset
I used the [Book Recommendation Dataset](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbV9JMWkwaExIRmJqYkFEZ2pIZVU0ZW5hdVYzd3xBQ3Jtc0ttbExscjRvNC1CWW1BaW5OLU1DSnRuS1FtRnl1LUQ3MU52M0k5U1BUcm9iU3FlNmRzMkFZaGxBNlZyQ251MVZwamI1NWVSOEtUT0xYMkIzMnJYd2VjS0hfZFU0d1BKSjdkSks5RDhKRTdIdU0wYUJJRQ&q=https%3A%2F%2Fwww.kaggle.com%2Fdatasets%2Farashnic%2Fbook-recommendation-dataset&v=1YoD0fg3_EM) for building this recommender system. 


## 🛠️ Data Preprocessing
 
- in this I have three different file
- I did extensive preprocessing and data cleaning using pandas and numpy.
- I used users threshold 250 and book-rating threshold 50 for collaborative filtering
- and for popularity, I suggested some books based on the average rating, considering atleast 250 num_ratings on a book. see this ```popular_50_books.csv``` for top 50 highly rated books.
 

 

## 📊 Inference
I created a script ```inference_movie_recommend_collaborative.py``` to run inference.
It checks the top five recommendations for any searched book in our database.

➡️ Just run the file with your input book and it will print the recommendations.

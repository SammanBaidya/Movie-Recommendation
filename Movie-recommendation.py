import pandas as pd
import pymysql
from sklearn.metrics.pairwise import cosine_similarity

# Connect to the MySQL database
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='chelsea$',
    database='movie_recommendation'
)

users_df = pd.read_sql('SELECT * FROM users', conn) #Loading data
movies_df = pd.read_sql('SELECT * FROM movies', conn)
ratings_df = pd.read_sql('SELECT * FROM ratings', conn)

# Close the connection
conn.close()

print("Users Data: \n", users_df)
print("movies Data:\n", movies_df)
print("Ratings Data: \n", ratings_df)

# Creating user item matrix; Value of the matrix will be ratings 
user_item_matrix = ratings_df.pivot(index = 'user_id', columns = 'movie_id', values = 'rating').fillna(0)
print("User-Item Matrix:\n", user_item_matrix)

# Calculates user similarity matrix using cosine similarity
#SimilArity matris created where each value represents the similarity of 2 users
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index = user_item_matrix.index, columns = user_item_matrix.index)
print("User Similarity Matrix:\n", user_similarity_df)

# Recommend movies Function
def recommend_movies(target_user_id, user_item_matrix, user_similarity_df, top_n=2):
    #Finding similar users by sorting the similarity score 
    similar_users = user_similarity_df[target_user_id].sort_values(ascending=False).index[1:]
    recommendations = pd.Series(dtype = 'float64')

#Each similar user get their rated movies and added to recommendation
    for user in similar_users:
        rated_movies = user_item_matrix.loc[user]
        recommendations = recommendations.append(rated_movies[rated_movies > 0])
#calculating average rating for each movie by users
    recommendations = recommendations.groupby(recommendations.index).mean()
    watched_movies = user_item_matrix.loc[target_user_id][user_item_matrix.loc[target_user_id] > 0].index
    recommendations = recommendations.drop(watched_movies, errors='ignore')
    
    return recommendations.sort_values(ascending=False).head(top_n)

# Recommendations for all 3 users
for target_user_id in [1, 2, 3]:
    recommended_movies = recommend_movies(target_user_id, user_item_matrix, user_similarity_df)
    
    recommendations = [
        (movies_df.loc[movies_df['movie_id'] == movie_id, 'title'].values[0], score)
        for movie_id, score in recommended_movies.items()
    ]
    print(f"Recommended movies for user {target_user_id}:")
    for title, score in recommendations:
        print(f" - {title}: {score:.2f}")
    print()
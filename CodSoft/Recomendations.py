import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Creating a sample user-movie ratings matrix
data = {
    'Movie A': [5, 4, 1, 3, 0],
    'Movie B': [3, 0, 1, 3, 4],
    'Movie C': [0, 4, 0, 4, 5],
    'Movie D': [1, 1, 5, 3, 2],
    'Movie E': [4, 5, 2, 3, 1]
}
ratings = pd.DataFrame(data, index=['User 1', 'User 2', 'User 3', 'User 4', 'User 5'])

# Compute cosine similarity between items (movies)
item_similarity = cosine_similarity(ratings.T)

# Create a DataFrame from the similarity matrix for easier reading
item_similarity_df = pd.DataFrame(item_similarity, index=ratings.columns, columns=ratings.columns)

# Function to recommend movies to a user based on the movies they have liked
def recommend_movies_item_based(user, ratings, item_similarity_df, n_recommendations=3):
    user_ratings = ratings.loc[user]
    rated_movies = user_ratings[user_ratings > 0].index.tolist()

    # If the user has not rated any movies, return an empty list
    if not rated_movies:
        return []

    # Calculate weighted scores for unrated movies based on rated ones
    weighted_scores = pd.Series(np.zeros(ratings.shape[1]), index=ratings.columns)

    for movie in rated_movies:
        # Add similarity scores for movies the user has rated
        weighted_scores += item_similarity_df[movie] * user_ratings[movie]

    # Filter out the movies the user has already rated
    unrated_movies = weighted_scores[user_ratings == 0]

    # Get the top N recommended movies
    recommendations = unrated_movies.sort_values(ascending=False)[:n_recommendations]

    return recommendations.index.tolist()

# Example: Recommend movies for 'User 1'
user = 'User 1'
recommended_movies_item_based = recommend_movies_item_based(user, ratings, item_similarity_df, n_recommendations=3)

print(f"Movies recommended for {user} (item-based): {recommended_movies_item_based}")

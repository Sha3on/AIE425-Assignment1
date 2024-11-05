import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the scraped data
scraped_data = pd.read_csv('scraped_user_item_ratings.csv')

# Create the user-item matrix by pivoting the data
user_item_matrix = scraped_data.pivot(index='User', columns='Item', values='Rating')
user_item_matrix = user_item_matrix.fillna(value=pd.NA)

# Arrange users from User_1 to User_50
user_item_matrix.index = pd.Categorical(user_item_matrix.index, categories=[f'User_{i}' for i in range(1, 51)], ordered=True)
user_item_matrix = user_item_matrix.sort_index()

# Step 1: User-Based Collaborative Filtering
user_pearson_corr = user_item_matrix.T.corr(method='pearson')
user_cosine_sim = pd.DataFrame(cosine_similarity(user_item_matrix.fillna(0)),
                                index=user_item_matrix.index, columns=user_item_matrix.index)

# Step 2: Item-Based Collaborative Filtering
item_pearson_corr = user_item_matrix.corr(method='pearson')
item_cosine_sim = pd.DataFrame(cosine_similarity(user_item_matrix.T.fillna(0)),
                                index=user_item_matrix.columns, columns=user_item_matrix.columns)

# Prediction Functions
def predict_user_based(user_item_matrix, user_pearson_corr):
    user_predictions = pd.DataFrame(index=user_item_matrix.index, columns=user_item_matrix.columns)
    for user in user_item_matrix.index:
        similar_users = user_pearson_corr[user].drop(user).dropna()
        similar_users = similar_users[similar_users > 0]
        for item in user_item_matrix.columns:
            if pd.isna(user_item_matrix.loc[user, item]):
                similar_ratings = user_item_matrix.loc[similar_users.index, item]
                similar_ratings = similar_ratings[similar_ratings.notna()]
                if not similar_ratings.empty:
                    weighted_sum = sum(similar_users[similar_ratings.index] * similar_ratings)
                    user_predictions.loc[user, item] = weighted_sum / similar_users[similar_ratings.index].sum()
    return user_predictions

def predict_item_based(user_item_matrix, item_pearson_corr):
    item_predictions = pd.DataFrame(index=user_item_matrix.index, columns=user_item_matrix.columns)
    for item in user_item_matrix.columns:
        for user in user_item_matrix.index:
            if pd.isna(user_item_matrix.loc[user, item]):
                similar_items = item_pearson_corr[item].drop(item).dropna()
                similar_items = similar_items[similar_items > 0]
                similar_ratings = user_item_matrix.loc[user, similar_items.index]
                similar_ratings = similar_ratings[similar_ratings.notna()]
                if not similar_ratings.empty:
                    weighted_sum = sum(similar_items[similar_ratings.index] * similar_ratings)
                    item_predictions.loc[user, item] = weighted_sum / similar_items[similar_ratings.index].sum()
    return item_predictions

# Generate predictions
user_based_predictions = predict_user_based(user_item_matrix, user_pearson_corr)
item_based_predictions = predict_item_based(user_item_matrix, item_pearson_corr)

# Save all results to a single text file
with open('predictions_and_similarities.txt', 'w') as f:
    f.write("User-Based Predictions:\n")
    f.write(user_based_predictions.to_string())
    f.write("\n\nItem-Based Predictions:\n")
    f.write(item_based_predictions.to_string())
    f.write("\n\nUser Pearson Correlation:\n")
    f.write(user_pearson_corr.to_string())
    f.write("\n\nUser Cosine Similarity:\n")
    f.write(user_cosine_sim.to_string())
    f.write("\n\nItem Pearson Correlation:\n")
    f.write(item_pearson_corr.to_string())
    f.write("\n\nItem Cosine Similarity:\n")
    f.write(item_cosine_sim.to_string())

print("All predictions and similarity matrices saved to predictions_and_similarities.txt.")



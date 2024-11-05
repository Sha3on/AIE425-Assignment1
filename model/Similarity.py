import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the pivoted user-item matrix
user_item_matrix = pd.read_csv('pivoted_user_item_ratings.csv', index_col=0)

# Step 1: User-Based Collaborative Filtering
# Calculate Pearson correlation for user-based similarity
user_pearson_corr = user_item_matrix.T.corr(method='pearson')

# Calculate cosine similarity for user-based similarity
user_cosine_sim = pd.DataFrame(cosine_similarity(user_item_matrix.fillna(0)),
                                index=user_item_matrix.index, columns=user_item_matrix.index)

# Step 2: Item-Based Collaborative Filtering
# Calculate Pearson correlation for item-based similarity
item_pearson_corr = user_item_matrix.corr(method='pearson')

# Calculate cosine similarity for item-based similarity
item_cosine_sim = pd.DataFrame(cosine_similarity(user_item_matrix.T.fillna(0)),
                                index=user_item_matrix.columns, columns=user_item_matrix.columns)

# Display the results
print("User-Based Pearson Correlation:")
print(user_pearson_corr.head())

print("\nUser-Based Cosine Similarity:")
print(user_cosine_sim.head())

print("\nItem-Based Pearson Correlation:")
print(item_pearson_corr.head())

print("\nItem-Based Cosine Similarity:")
print(item_cosine_sim.head())

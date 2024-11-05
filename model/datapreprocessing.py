import pandas as pd

# Load the pivoted user-item matrix
pivoted_data = pd.read_csv('pivoted_user_item_ratings.csv', index_col=0)

# Compute the average rating for each user (row-wise)
user_avg_ratings = pivoted_data.mean(axis=1)
print("Average rating for each user:")
print(user_avg_ratings.head())

# Compute the average rating for each item (column-wise)
item_avg_ratings = pivoted_data.mean(axis=0)
print("\nAverage rating for each item:")
print(item_avg_ratings.head())

# Save the average ratings to CSV files
user_avg_ratings.to_csv('user_average_ratings.csv', header=['Average Rating'])
item_avg_ratings.to_csv('item_average_ratings.csv', header=['Average Rating'])

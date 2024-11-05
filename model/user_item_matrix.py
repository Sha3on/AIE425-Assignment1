import pandas as pd

# Load the pivoted user-item matrix
user_item_matrix = pd.read_csv('pivoted_user_item_ratings.csv', index_col=0)

# Display the user-item matrix to confirm it is structured correctly
print("User-Item Matrix:")
print(user_item_matrix.head())

# Check for any missing values
missing_values = user_item_matrix.isnull().sum()
print("\nMissing values per column:")
print(missing_values)

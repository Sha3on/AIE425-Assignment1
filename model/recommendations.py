import pandas as pd

# Load the user-based predictions from the CSV file
user_based_predictions = pd.read_csv('user_based_predictions.csv', index_col=0)

# Load the item-based predictions from the CSV file
item_based_predictions = pd.read_csv('item_based_predictions.csv', index_col=0)

# Function to get top N recommendations
def get_top_n_recommendations(predictions, n=5):
    top_n_recommendations = {}
    for user in predictions.index:
        user_predictions = predictions.loc[user]
        unrated_items = user_predictions[user_predictions.isna()]  # Filter out rated items
        top_n_items = unrated_items.nlargest(n).index.tolist()  # Get top N items
        top_n_recommendations[user] = top_n_items
    return top_n_recommendations

# Get top N recommendations using user-based predictions
top_n_user_based = get_top_n_recommendations(user_based_predictions, n=5)

# Get top N recommendations using item-based predictions
top_n_item_based = get_top_n_recommendations(item_based_predictions, n=5)

# Save recommendations to a text file
with open('recommendations.txt', 'w') as f:
    # User-Based Recommendations
    f.write("Top N Recommendations (User-Based):\n")
    for user, items in top_n_user_based.items():
        f.write(f"{user}: {items}\n")
    
    f.write("\n")

    # Item-Based Recommendations
    f.write("Top N Recommendations (Item-Based):\n")
    for user, items in top_n_item_based.items():
        f.write(f"{user}: {items}\n")

print("All recommendations saved to recommendations.txt.")

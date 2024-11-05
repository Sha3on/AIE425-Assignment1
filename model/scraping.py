import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

# Base URL of the website to scrape
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# Initialize a list to store book data
books = []

# Scrape the first few pages to collect book data (adjust range as needed)
for page in range(1, 3):  # Adjust page range to collect enough data
    url = base_url.format(page)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all book containers on the page
        for book in soup.find_all('article', class_='product_pod'):
            title = book.h3.a['title']
            books.append(title)
    else:
        print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
    
    # Pause to prevent overwhelming the server
    time.sleep(1)

# Ensure we have at least 25 unique books for the dataset
books = books[:25]

# Generate data for at least 50 users rating at least 22 out of 25 books
users = []
items = []
ratings = []

# Create data for 50 users
for user_id in range(1, 51):
    user = f"User_{user_id}"
    # Each user rates at least 22 out of 25 books
    rated_books = random.sample(books, 22)
    
    for book in rated_books:
        users.append(user)
        items.append(book)
        ratings.append(random.randint(1, 5))  # Random rating between 1 and 5

# Create a DataFrame from the generated data
scraped_data = pd.DataFrame({
    'User': users,
    'Item': items,
    'Rating': ratings
})

# Display the DataFrame
print(scraped_data.head())

# Save the DataFrame to a CSV file
scraped_data.to_csv('scraped_user_item_ratings.csv', index=False)

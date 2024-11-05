# AIE425-Assignment1


Book Recommendation System

Overview
This project implements a book recommendation system using collaborative filtering techniques. The system scrapes user ratings data from the Books to Scrape website, processes the data, and utilizes both user-based and item-based collaborative filtering to provide personalized book recommendations.

Features
- Web Scraping: Collect user ratings and book information from the Books to Scrape website.
- Data Preprocessing: Handle missing values and structure the data into a user-item matrix.
- User-Based Collaborative Filtering: Predict ratings based on similarities between users.
- Item-Based Collaborative Filtering: Recommend books that are similar to those rated highly by users.
- Interactive User Interface: Built with Streamlit for easy access and interaction with the recommendations.

Installation
To get started with this project, follow these steps:

1. Clone the repository or download the source code to your local machine.
2. Navigate to the project directory in your terminal or command prompt.
3. Install the required libraries using pip:
   pip install -r requirements.txt
4. Run the Streamlit application with the following command:
   streamlit run app.py

Usage
After running the application, open your web browser and go to http://localhost:8501 to access the book recommendation system. You can input your preferences and receive personalized book suggestions.

Requirements
This project requires the following Python libraries:
- pandas
- numpy
- scikit-learn
- streamlit
- requests
- beautifulsoup4

Feel free to explore and enjoy discovering new books!

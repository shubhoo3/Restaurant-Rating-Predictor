# Restaurant Rating Predictor

The Restaurant Rating Predictor is a machine learning-based web application that predicts restaurant ratings based on various input features. This project utilizes Python, Streamlit, and Scikit-learn to build and deploy the model in an interactive and user-friendly interface.




## Features

1.  User-friendly Streamlit web interface for rating prediction.


2. Utilizes Scikit-learn for building and training the machine learning model.

3. Predicts restaurant ratings based on features such as location, cuisine, reviews, and other relevant factors.

4. Easy-to-use input fields for users to enter data and get real-time predictions.


 

## Dataset

This dataset is designed for developing a machine learning model to classify restaurants based on their cuisines. It includes various attributes related to restaurants such as location, average cost, ratings, and services offered. The primary objective is to predict the cuisine type of a restaurant using these attributes.

1. **Restaurant ID**: Unique identifier for each restaurant.
2. **Restaurant Name**: Name of the restaurant.
3. **Country Code**: Country code where the restaurant is located.
4. **Cuisines**: Type of cuisines offered by the restaurant (target variable).
5. **Average Cost for Two**: Average cost for two people dining at the restaurant.
6. **Has Table Booking**: Binary variable indicating if the restaurant accepts table bookings.
7. **Has Online Delivery**: Binary variable indicating if the restaurant offers online delivery.
8. **Price Range**: Range indicating the price level of the restaurant's menu items.
9. **Aggregate Rating**: Average rating of the restaurant based on customer reviews.


## Steps


- **Clone the repository**: https://github.com/shubhoo3/Restaurant-Rating-Predictor.git


- **Create and activate a virtual environment (optional but recommended)**: python -m venv venv 

- **Run the Streamlit app**: streamlit run app.py


## Technologies Used

**Python:** Core programming language.

**Streamlit:** For building the interactive web application.

**Scikit-learn:** For implementing machine learning algorithms.

**Pandas & NumPy:** For data manipulation and preprocessing.

**Matplotlib & Seaborn:** For data visualization (if applicable).

## Model Training

The dataset is preprocessed using Pandas and Scikit-learn.

Feature selection and transformation are applied.

A machine learning model (e.g., Linear Regression, Random Forest, or XGBoost) is trained and evaluated.

The best-performing model is saved and used for predictions.

## Future Improvements

Enhance the model accuracy by experimenting with different algorithms.

Add more features such as sentiment analysis from customer reviews.

Deploy the application on a cloud platform like Heroku or AWS.

Improve UI/UX for better user experience.



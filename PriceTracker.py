import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.linear_model import LinearRegression
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def get_product_info(url):
    # Send the GET request to the URL with the headers
    response = requests.get(url, headers=headers)

    # Check if the response was successful
    if response.status_code != 200:
        print(f"The request was not successful. Status code: {response.status_code}")
        exit()

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    if 'amazon.in' in url:
        # Find the product name
        product_name_element = soup.find('span', {'id': 'productTitle'})
        if product_name_element:
            product_name = product_name_element.text.strip()

        # Find the product price
        product_price_element = soup.find('span',{'class':'a-price-whole'})
        if product_price_element:
            product_price_str = product_price_element.text.strip().replace(",", "")
            product_price = float(product_price_str)
            
        # Determine the best time to buy the product
        buying_time = determine_buying_time()

        return {"product_name": product_name, "product_price": product_price, "buying_time": buying_time}
    
    elif 'flipkart.com' in url:
        # Find the product name
        product_name_element = soup.find("span", {"class": "B_NuCI"})
        product_name = product_name_element.text.strip()

        # Find the product price
        product_price_element= soup.find('div',{'class': '_30jeq3 _16Jk6d'})
        product_price_str = product_price_element.text.strip().replace(",","")
        product_price_str = product_price_str.replace("₹", "")
        product_price = float(product_price_str)

        # Determine the best time to buy the product
        buying_time = determine_buying_time()

        return {"product_name": product_name, "product_price": product_price, "buying_time": buying_time}
    
    elif 'snapdeal.com' in url:
        # Find the element containing the product name
        product_name_element = soup.find('h1', {'class': 'pdp-e-i-head'})

        # Extract the product name
        product_name = product_name_element.text.strip()

        # Find the element containing the product price
        price_element = soup.find('span', {'class': 'payBlkBig'})

        # Extract the price value
        product_price = re.sub('[^0-9]+', '', price_element.text.strip())

        # Determine the best time to buy the product
        buying_time = determine_buying_time()

        return {"product_name": product_name, "product_price": product_price, "buying_time": buying_time}

def determine_buying_time():
    # Load dataset of product prices over time
    df = pd.read_csv('product_prices.csv', parse_dates=['current_time'])

    # Create a column for days since release
    df['days_since_release'] = (df['current_time'] - pd.to_datetime('2023-03-10')).dt.days

    # Split the dataset into training and testing sets
    train = df[df['current_time'] < '2024-01-01']
    test = df[df['current_time'] >= '2023-01-01']

    # Create a linear regression model and train it on the training set
    model = LinearRegression()
    model.fit(train[['days_since_release']], train['product_price'])

    # Use the trained model to make predictions on the testing set
    predictions = model.predict(test[['days_since_release']])

    # Calculate the mean squared error of the predictions
    mse = ((predictions - test['product_price']) ** 2).mean()

    # Determine if it's a good time to buy the product based on the mean squared error
    if mse < 100:
        return "This is absolutely the best time to buy this product. Don't miss out, Drop chances are lower than 15%"
    elif mse < 1000:
        return "This is a great time to buy this product. Drop chances are very rare and price is unlikely to drop for this product."
    elif mse < 10000:
        return "Price is likely to be dropped for this product. You should wait for a little more to save some money."
    else:
        return "You should absolutely wait for a price drop. Price seems higher than average and drop chances are above 80%"
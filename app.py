from flask import Flask, redirect, request, render_template
from PriceTracker import get_product_info
import smtplib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            scraped_data = get_product_info(url)
            if "error" in scraped_data:
                return render_template('error.html', error=scraped_data["error"])
            else:
                product_name = scraped_data["product_name"]
                product_price = scraped_data["product_price"]
                buying_time = scraped_data["buying_time"]
                return render_template('result.html', product_name=product_name, product_price=product_price, buying_time=buying_time)
        else:
            return notify()
    else:
        return render_template('index.html')
        # your existing code to scrape the URL goes here


@app.route('/notify', methods=['GET', 'POST'])
def notify():
    if request.method == 'POST':
        desired_price = float(request.form['DesiredPrice'])
        to_email = request.form['UserEmail']
        # implement this function to get the product price
        url1 = request.form['url1']
        product_name = get_product_info(url1)
        product_price = get_product_info(url1)
        product_name_element = product_name["product_name"]
        product_price_element = float(product_price["product_price"])
        if product_price is not None and product_price_element <= desired_price:
            send_notification(desired_price, product_price_element, to_email, url1)
            return render_template('success.html', product_name=product_name_element, desired_price=desired_price, product_price=product_price_element, to_email=to_email )
        else:
            return render_template('failure.html', product_name=product_name_element, desired_price=desired_price, product_price=product_price_element, to_email=to_email)
    else:
        return render_template('index.html')


def send_notification(desired_price, product_price_element, to_email, url1):
    message = f"Subject: Price Alert: Your Product Price is Fallen!\n\nThe price of the product at {url1} has fallen below {desired_price} . \nThe current price is {product_price_element}."
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('priteshsdhumal03@gmail.com', 'wqaw tywq tmuc atir')
    server.sendmail('priteshsdhumal03@gmail.com', to_email, message)
    server.quit()


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, redirect, request, render_template
from PriceTracker import get_product_info
import smtplib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            scraped_data = get_product_info(url)
            if "error" in scraped_data:
                return render_template('error.html', error=scraped_data["error"])
            else:
                product_name = scraped_data["product_name"]
                product_price = scraped_data["product_price"]
                buying_time = scraped_data["buying_time"]
                return render_template('result.html', product_name=product_name, product_price=product_price, buying_time=buying_time)
        else:
            return notify()
    else:
        return render_template('index.html')
        # your existing code to scrape the URL goes here


@app.route('/notify', methods=['GET', 'POST'])
def notify():
    if request.method == 'POST':
        desired_price = float(request.form['DesiredPrice'])
        to_email = request.form['UserEmail']
        # implement this function to get the product price
        url1 = request.form['url1']
        product_name = get_product_info(url1)
        product_price = get_product_info(url1)
        product_name_element = product_name["product_name"]
        product_price_element = float(product_price["product_price"])
        if product_price is not None and product_price_element <= desired_price:
            send_notification(desired_price, product_price_element, to_email, url1)
            return render_template('success.html', product_name=product_name_element, desired_price=desired_price, product_price=product_price_element, to_email=to_email )
        else:
            return render_template('failure.html', product_name=product_name_element, desired_price=desired_price, product_price=product_price_element, to_email=to_email)
    else:
        return render_template('index.html')


def send_notification(desired_price, product_price_element, to_email, url1):
    message = f"Subject: Price Alert: Your Product Price is Fallen!\n\nThe price of the product at {url1} has fallen below {desired_price} . \nThe current price is {product_price_element}."
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('priteshsdhumal03@gmail.com', 'aarqbpmdlugjqplb')
    server.sendmail('priteshsdhumal03@gmail.com', to_email, message)
    server.quit()


if __name__ == '__main__':
    app.run(debug=True)

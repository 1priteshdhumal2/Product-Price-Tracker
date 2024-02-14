# Online Product Price Tracker

This project is a web-based tool built with Flask that allows users to track product prices from various e-commerce websites like Amazon, Flipkart, and Snapdeal. It helps users monitor price changes and notifies them when a desired price is reached.

## Features

- **Price Tracking:** Track product prices from Amazon, Flipkart, and Snapdeal.
- **Price Notifications:** Receive email notifications when a product's price reaches a user-set threshold.
- **Best Buying Time Prediction:** Predicts the best time to buy a product based on historical price data.

## Installation

### Prerequisites

- Python 3.x
- Install required Python packages:
  ```bash
  pip install Flask requests beautifulsoup4 pandas scikit-learn
  ```

### Running the Application

1. Clone the repository:
   ```bash
   git clone <repository_URL.git>
   cd Online-Product-Price-Tracker
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Usage

- **Home Page:** Enter the URL of the product you want to track and view its details.
- **Notify Page:** Set a desired price and your email to receive notifications when the product's price drops.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any new features, bug fixes, or improvements.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to add more sections or details specific to your project's requirements or guidelines for contributors. Adjust the installation and usage instructions if necessary to match your project's setup.

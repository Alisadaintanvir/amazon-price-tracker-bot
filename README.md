# Amazon Price Tracker

#### This is a simple Amazon price tracker that checks the current price of a product and sends an email notification if the price drops below a certain threshold.

## Features

- Fetches the current price of a specified Amazon product.
- Sends an email notification if the price drops below a target threshold.
- Utilizes the Amazon Product Advertising API to retrieve product information.
- Sends email notifications using the Gmail SMTP server.

## Usage

1. Clone this repository to your local machine.

`git clone https://github.com/Alisadaintanvir/amazon-price-tracker.git
cd amazon-price-tracker`


Certainly! Here's a simple README.md file that you can use on GitHub for your project:

markdown
Copy code
# Amazon Price Tracker

This is a simple Amazon price tracker that checks the current price of a product and sends an email notification if the price drops below a certain threshold.

## Features

- Fetches the current price of a specified Amazon product.
- Sends an email notification if the price drops below a target threshold.
- Utilizes the Amazon Product Advertising API to retrieve product information.
- Sends email notifications using the Gmail SMTP server.

## Usage

1. Clone this repository to your local machine.

`git clone https://github.com/yourusername/amazon-price-tracker.git
cd amazon-price-tracker`

2. Install the required Python packages.

`pip install -r requirements.txt`

3. Set up your environment variables in a .env file. You'll need to provide your Gmail email and password for sending notifications.

`GMAIL_EMAIL=your@gmail.com
GMAIL_PASSWORD=yourpassword`

4. Modify the main.py file to set your desired product URL and target price.
 
`PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?ref=..."
target_price = 70`

5. Run the script to start tracking the price and sending notifications.

`python main.py`

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was inspired by the need to track Amazon product prices and receive notifications.
Built with love and Python.

import requests
from bs4 import BeautifulSoup
import lxml


class PriceTracker:
    def __init__(self, url):
        self.url = url
        self.title = None

    def request(self):
        header = {
            "sec-ch-ua-platform": "Windows",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/115.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                      "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        }

        response = requests.get(url=self.url, headers=header)
        response.raise_for_status()
        data = response.text
        soup = BeautifulSoup(data, "lxml")
        price_in_dollar = soup.select_one(".a-price-whole").getText()
        price_in_cent = soup.select_one(".a-price-fraction").getText()
        self.title = soup.select_one("#productTitle").getText()

        total_price = float(price_in_dollar + price_in_cent)
        return total_price

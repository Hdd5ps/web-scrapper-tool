import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def fetch_html(self):
        self.driver.get(self.url)
        time.sleep(3)  # Wait for dynamic content to load
        html = self.driver.page_source
        return html

    def close_driver(self):
        self.driver.quit()

    def scrape(self):
        html = self.fetch_html()
        soup = BeautifulSoup(html, 'html.parser')
        # Example: Extract product names, prices, and descriptions
        products = []
        for item in soup.select('.product-item'):
            name = item.select_one('.product-name').get_text(strip=True)
            price = item.select_one('.product-price').get_text(strip=True)
            description = item.select_one('.product-description').get_text(strip=True)
            products.append({
                'name': name,
                'price': price,
                'description': description
            })
        self.close_driver()
        return products
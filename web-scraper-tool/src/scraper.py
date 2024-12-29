import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class WebScraper:
    def __init__(self, url):
        self.url = url
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def fetch_html(self):
        try:
            self.driver.get(self.url)
            # Wait for the dynamic content to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.product-item'))
            )
            html = self.driver.page_source
            return html
        except Exception as e:
            print(f"Error fetching HTML: {e}")
            return None

    def close_driver(self):
        self.driver.quit()

    def scrape(self):
        html = self.fetch_html()
        if not html:
            return []

        soup = BeautifulSoup(html, 'html.parser')
        products = []
        for item in soup.select('.product-item'):
            name = item.select_one('.product-name')
            price = item.select_one('.product-price')
            description = item.select_one('.product-description')

            products.append({
                'name': name.get_text(strip=True) if name else "N/A",
                'price': price.get_text(strip=True) if price else "N/A",
                'description': description.get_text(strip=True) if description else "N/A"
            })
        self.close_driver()
        return products

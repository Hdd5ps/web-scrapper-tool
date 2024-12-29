from bs4 import BeautifulSoup

class Parser:
    def __init__(self, html_content):
        if not html_content:
            raise ValueError("HTML content cannot be empty or None")
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def parse_product_names(self):
        try:
            product_names = [tag.text.strip() for tag in self.soup.find_all(class_='product-name')]
            return product_names if product_names else ["No product names found"]
        except Exception as e:
            return [f"Error parsing product names: {e}"]

    def parse_prices(self):
        try:
            prices = [tag.text.strip() for tag in self.soup.find_all(class_='product-price')]
            return prices if prices else ["No prices found"]
        except Exception as e:
            return [f"Error parsing prices: {e}"]

    def parse_descriptions(self):
        try:
            descriptions = [tag.text.strip() for tag in self.soup.find_all(class_='product-description')]
            return descriptions if descriptions else ["No descriptions found"]
        except Exception as e:
            return [f"Error parsing descriptions: {e}"]

    def parse_all(self):
        return {
            "product_names": self.parse_product_names(),
            "prices": self.parse_prices(),
            "descriptions": self.parse_descriptions()
        }

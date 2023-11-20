from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import json

def process_product(prod):
    discount = prod['price_range']['minimum_price']['discount']['percent_off']
    amount_off = prod['price_range']['minimum_price']['discount']['amount_off']
    initial_price = prod['price_range']['minimum_price']['regular_price']['value']
    final_price = prod['price_range']['minimum_price']['final_price']['value']
    in_stock = prod['stock_status']

    return {
        'Product': prod['name'], 
        'Discount': discount, 
        'Amount Off': amount_off, 
        'Regular Price': initial_price, 
        'Special Price': final_price,
        'In Stock': in_stock
    }

def main():
    url = "https://www.pcdiga.com/api/getProducts/computadores-e-software?pagina={page}"

    driver = webdriver.Chrome()
    products = []

    try:
        driver.get(url.format(page=1))
        time.sleep(5)  # Wait for page to load

        jsonResponse = json.loads(driver.find_element(By.TAG_NAME, "body").text)
        total_pages = jsonResponse["pageInfo"]["total_pages"]

        for page in range(1, 1 + 1):
            driver.get(url.format(page=page))
            time.sleep(5)  
            jsonResponse = json.loads(driver.find_element(By.TAG_NAME, "body").text)
            products_list = jsonResponse['filtered_prods']

            for prod in products_list:
                if prod['price_range']['minimum_price']['discount']['percent_off'] > 0:
                    products.append(process_product(prod))
                    
    except Exception as e:
        print(e)

    finally:
        driver.quit()

    df = pd.DataFrame(products).sort_values(by=['Amount Off'], ascending=False).reset_index(drop=True)
    df.to_csv('pcdiga.csv', index=False)

if __name__ == "__main__":
    main()
# Discounts Website Data Scraper

## Introduction
This repository contains a folder, with one Python script, for scraping discounted product data from PC Diga's website. 

## Script Overview

The `pcdiga_discount_scraper.py` script, located in the `pcdiga_web_scraper` folder, accesses the PCDIGA API for computers and software products. It specifically targets products with active discounts, extracts relevant details like product name, discount percentage, original price, discounted price, and stock status, compiles the data, and saves it as CSV file.

## Requirements
- Python 3
- Libraries: `Selenium WebDriver`, `pandas`

## How to Run
1. Clone the repository or download the scripts.
   ```bash
   git clone git@github.com:Fredd124/Discount-Web-Scrapper.git
   cd Discount-Web-Scrapper
2. Install the required Python libraries:
   ```bash
   pip install selenium pandas
   ````
3. Run the script of your choice, inside of its folder:
   ```bash
   python3 best_discounts_pcdiga.py
   ```
   
## Observations

* The script opens a browser window via WebDriver, allowing you to visually and track the scraping process.
* The script is currently set up to scrape data from a specific URL. However, users can modify the URL to scrape different product categories by referencing alternative URLs listed in the `alternative_urls.txt` file included in the repository. This feature allows for greater flexibility in the type of product data being scraped.
* Ensure a stable internet connection for the script to run without interruptions.

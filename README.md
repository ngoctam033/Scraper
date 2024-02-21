### README
###Introduction
This Python script is designed to scrape product information from the FPTShop website (https://fptshop.com.vn/may-tinh-xach-tay) using Selenium and BeautifulSoup libraries. It automates the process of clicking the "Xem thêm" (Load More) button to retrieve all available products and extracts their names and prices.

Prerequisites
Python 3.x
Selenium library (pip install selenium)
BeautifulSoup library (pip install beautifulsoup4)
Usage
Make sure you have the required libraries installed.
Run the script product_scraper.py.
The script will open a Firefox browser, navigate to the FPTShop laptop page, and start scraping product information.
It will print out the name and price of each product, as well as the total number of products scraped.
Code Explanation
The script initializes a Firefox WebDriver using Selenium.
It navigates to the FPTShop laptop page.
It clicks the "Xem thêm" button repeatedly until all products are loaded.
The HTML content of the page is extracted using Selenium.
BeautifulSoup is used to parse the HTML content.
Product information (name and price) is extracted from the parsed HTML.
The WebDriver is closed after scraping is complete.
Additional Resources
Selenium Documentation
BeautifulSoup Documentation
Note
Ensure that you have a stable internet connection while running the script to avoid interruptions in web scraping.

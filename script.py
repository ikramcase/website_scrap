import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time

# Initialize the Selenium web driver
driver = webdriver.Chrome(executable_path="path/to/chromedriver")

# Navigate to the website
driver.get("https://www.injuredgadgets.com")

# Locate the element that leads to iPhone screens and cameras
iphone_parts_link = driver.find_element(By.PARTIAL_LINK_TEXT, "iPhone Parts")
iphone_parts_link.click()

# Extract pricing information
data = []
for category in ["iPhone Screens", "Front Cameras", "Back Cameras"]:
    category_link = driver.find_element(By.PARTIAL_LINK_TEXT, category)
    category_link.click()
    
    products = driver.find_elements(By.CLASS_NAME, "collection-product")
    for product in products:
        name = product.find_element(By.CLASS_NAME, "collection-product-title").text
        price = product.find_element(By.CLASS_NAME, "money").text
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data.append([timestamp, category, name, price])

# Create a pandas dataframe
columns = ["Timestamp", "Category", "Product Name", "Price"]
df = pd.DataFrame(data, columns=columns)

# Save the dataframe to an Excel file
df.to_excel("pricing_data.xlsx", index=False)

# Close the web browser
driver.quit()

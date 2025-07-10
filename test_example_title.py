from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Setup
service = Service()
driver = webdriver.Chrome(service=service)

# Step 1: Open site
driver.get("https://example.com")
time.sleep(2)

# Step 2: Validate title
expected_title = "Example Domain"
actual_title = driver.title

if actual_title == expected_title:
    print("PASS: Title matches")
else:
    print(f"FAIL: Expected '{expected_title}', but got '{actual_title}'")

# Step 3: Close browser
driver.quit()

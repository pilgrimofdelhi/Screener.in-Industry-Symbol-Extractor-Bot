from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import re
import time
import csv   

chromedriver_path = r"D:\Python Bots..."                   #Replace with your browser location    
brave_path = r"C:\Program Files..."                        #Replace with your Chromedrive location                    
profile_path = r"D:\Python Bots..."                        #Replace with your Selenum profile          

options = Options()
options.binary_location = brave_path
options.add_argument(f'--user-data-dir={profile_path}')
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

with open(r"D:\Python Bots\screener_bot\links.txt", "r", encoding="utf-8") as f:
    links = [line.strip() for line in f if line.strip()]

rows_for_csv = []

for url in links:
    print(f"\nVisiting: {url}")
    try:
        driver.get(url)
        cat_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card h1")))
        category = cat_elem.text.strip()
        print("Category:", category)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".data-table.text-nowrap tbody tr")))
        rows = driver.find_elements(By.CSS_SELECTOR, ".data-table.text-nowrap tbody tr")
        print(f"Total rows found: {len(rows)}")
        symbols = []

        for i, row in enumerate(rows):
            cells = row.find_elements(By.CSS_SELECTOR, "td")
            if len(cells) < 2:
                continue
            try:
                link_elem = cells[1].find_element(By.TAG_NAME, "a")
                href = link_elem.get_attribute("href")
            except Exception:
                continue

            # Extraction logic
            m = re.search(r"/company/(\d+)/", href)
            if m:
                symbols.append(m.group(1))
                continue
            m = re.search(r"/company/([A-Z0-9]+)/consolidated/?", href)
            if m:
                symbols.append(m.group(1))
                continue
            m = re.search(r"/company/([A-Z0-9]+)/?$", href)
            if m:
                symbols.append(m.group(1))
                continue

        print(f"Extracted symbols: {symbols}")
        if symbols:
            rows_for_csv.append([category] + symbols)

    except Exception as e:
        print(f"Error processing {url}: {e}")

    # <--- Delay should be here, outside try/except, so it's always applied
    time.sleep(5)

# --- Write to CSV ---
with open("screener_symbols.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in rows_for_csv:
        writer.writerow(row)
print("\nSaved all results to screener_symbols.csv")

driver.quit()

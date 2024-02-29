from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create Chrome options
chrome_options = Options()

# Set up Chrome driver without executable path
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to website
    driver.get("https://www.prothomalo.com/topic/%E0%A6%95%E0%A6%AC%E0%A6%BF%E0%A6%A4%E0%A6%BE-%E0%A6%85%E0%A6%A8%E0%A7%8D%E0%A6%AF-%E0%A6%86%E0%A6%B2%E0%A7%8B")
    
    print("autosave checking")
    print(driver.title)
    
    # Wait for user input before closing the browser
    input("Press Enter to close the browser...")
except Exception as e:
    print('An error occurred: ', str(e))
finally:
    driver.quit()

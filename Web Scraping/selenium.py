#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

class SeleniumAutomation:
    def __init__(self):
        # Initialize Chrome driver
        # Make sure you have ChromeDriver installed: https://chromedriver.chromium.org/
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def example_1_google_search(self):
        """Example 1: Search on Google"""
        print("=== Example 1: Google Search ===")
        self.driver.get("https://www.google.com")
        
        # Find search box and enter text
        search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("Selenium Python")
        search_box.submit()
        
        # Wait for results
        time.sleep(2)
        print(f"Page title: {self.driver.title}")
    
    def example_2_click_button(self):
        """Example 2: Click buttons and navigate"""
        print("\n=== Example 2: Click Button ===")
        self.driver.get("https://www.wikipedia.org")
        
        # Find and click element
        try:
            english_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "English")))
            english_link.click()
            time.sleep(2)
            print(f"Navigated to: {self.driver.current_url}")
        except Exception as e:
            print(f"Error: {e}")
    
    def example_3_form_filling(self):
        """Example 3: Fill and submit a form"""
        print("\n=== Example 3: Form Filling ===")
        self.driver.get("https://www.wikipedia.org")
        
        # Find search input and type
        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "searchInput")))
        search_input.clear()
        search_input.send_keys("Python programming")
        
        # Find and click search button
        search_button = self.driver.find_element(By.ID, "searchButton")
        search_button.click()
        
        time.sleep(2)
        print(f"Search completed. Current URL: {self.driver.current_url}")
    
    def example_4_get_page_info(self):
        """Example 4: Extract page information"""
        print("\n=== Example 4: Get Page Info ===")
        self.driver.get("https://www.wikipedia.org")
        
        # Get page title
        title = self.driver.title
        print(f"Page Title: {title}")
        
        # Get page URL
        url = self.driver.current_url
        print(f"Page URL: {url}")
        
        # Get all links
        links = self.driver.find_elements(By.TAG_NAME, "a")
        print(f"Total links on page: {len(links)}")
        
        # Get first 5 link texts
        print("First 5 links:")
        for link in links[:5]:
            if link.text:
                print(f"  - {link.text}")
    
    def example_5_wait_for_element(self):
        """Example 5: Wait for elements to load"""
        print("\n=== Example 5: Wait for Element ===")
        self.driver.get("https://www.google.com")
        
        # Explicit wait for element
        search_box = self.wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        print("Search box found and ready!")
        
        # Send keys
        search_box.send_keys("Selenium WebDriver")
        search_box.submit()
        
        # Wait for results to load
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "g")))
        print("Results loaded!")
    
    def example_6_take_screenshot(self):
        """Example 6: Take screenshots"""
        print("\n=== Example 6: Take Screenshot ===")
        self.driver.get("https://www.python.org")
        
        # Take full page screenshot
        screenshot_path = "/tmp/webpage_screenshot.png"
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
    
    def example_7_get_element_attributes(self):
        """Example 7: Get element attributes"""
        print("\n=== Example 7: Get Element Attributes ===")
        self.driver.get("https://www.wikipedia.org")
        
        # Find element and get attributes
        logo = self.driver.find_element(By.CLASS_NAME, "mw-logo-container")
        
        # Get text content
        text = logo.text
        print(f"Element text: {text}")
        
        # Get attribute
        if logo.get_attribute("class"):
            print(f"Element class: {logo.get_attribute('class')}")
        
        # Get tag name
        print(f"Tag name: {logo.tag_name}")
    
    def close(self):
        """Close the browser"""
        self.driver.quit()
        print("\nBrowser closed.")

def main():
    automation = SeleniumAutomation()
    
    try:
        # Run examples
        automation.example_1_google_search()
        time.sleep(2)
        
        automation.example_2_click_button()
        time.sleep(2)
        
        automation.example_3_form_filling()
        time.sleep(2)
        
        automation.example_4_get_page_info()
        time.sleep(2)
        
        automation.example_5_wait_for_element()
        time.sleep(2)
        
        automation.example_6_take_screenshot()
        time.sleep(2)
        
        automation.example_7_get_element_attributes()
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        automation.close()

if __name__ == "__main__":
    main()
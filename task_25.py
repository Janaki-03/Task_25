from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# Set up the Chrome WebDriver
chrome_path = 'path/to/chromedriver'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the IMDb search page
driver.get("https://www.imdb.com/search/name/")

# Define the data to be filled in the input boxes, select boxes, and dropdown menu
name_input = "rock"
birth_date_input = "Your Birth Date"
birth_place_input = "Your Birth Place"
profession_dropdown_value = "Actor"
gender_select_value = "Male"

# Find and fill the input boxes
name_field = driver.find_element(By.ID, '//*[@id="accordion-item-nameTextAccordion"]/div/div/div')
name_field.send_keys(name_input)
sleep(4)
birth_date_field = driver.find_element(By.ID, '//*[@id="text-input__8"]')
birth_date_field.send_keys(birth_date_input)
sleep(4)

birth_place_field = driver.find_element(By.ID, '')
birth_place_field.send_keys(birth_place_input)

# Select values from dropdowns
profession_dropdown = driver.find_element(By.ID, "profession-dropdown")
profession_dropdown.click()
profession_option = driver.find_element(By.XPATH, f"//option[text()='{profession_dropdown_value}']")
profession_option.click()

gender_select = driver.find_element(By.ID, "gender-select")
gender_select.click()
gender_option = driver.find_element(By.XPATH, f"//option[text()='{gender_select_value}']")
gender_option.click()

# Wait for the search button to be clickable
search_button = driver.find_element(By.ID, "searchButton")
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, "searchButton")))

# Click the search button
search_button.click()

# Close the browser window
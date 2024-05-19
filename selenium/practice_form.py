from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

def delete_overlay(driver, element_id = str):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, element_id)))
    element = driver.find_element(By.ID, element_id)
    driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)

def click_id(driver, id):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, id)))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

def enter_text_name(driver, name, text):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.NAME, name)))
    driver.find_element(By.NAME, name).send_keys(text)

def enter_text_id(driver, id, text):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, id)))
    driver.find_element(By.ID, id).send_keys(text)

def select_dropdown(driver, id, option):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, id)))
    select = Select(element)
    select.select_by_visible_text(option)

def upload_file_id(driver, id, path_to_file):
    driver.find_element(By.ID, id).send_keys(path_to_file)

if __name__ == "__main__":
    options = Options()

    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    print("start testing with selenium")
    timeout = 30
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    #open URL
    driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
    time.sleep(3)
    
    #Accept cookies
    click_id(driver, "ez-accept-all" )
    time.sleep(3)

    #Remove overlay
    delete_overlay(driver, "gpt_unit_/1254144,22662382379/techlistic_com-pixel1_0")
    time.sleep(3)

    #Fill in form
    enter_text_name(driver, "firstname", "Safian")
    time.sleep(3)
    enter_text_name(driver, "lastname", "Khan")
    time.sleep(3)
    click_id(driver, "sex-0")
    time.sleep(3)
    click_id(driver, "exp-3")
    time.sleep(3)
    enter_text_id(driver, "datepicker", r"20/10/2025")
    time.sleep(3)
    click_id(driver, "profession-1")
    time.sleep(3)
    click_id(driver, "tool-2")
    time.sleep(3)
    select_dropdown(driver, "continents", "North America")
    time.sleep(3)
    select_dropdown(driver, "selenium_commands", "Navigation Commands" )
    time.sleep(3)
    upload_file_id(driver, "photo", r"C:\Users\Safian\OneDrive\Pictures\sample.PNG" )
    time.sleep(3)
    click_id(driver, "tool-2")
    time.sleep(3)
    click_id(driver, "submit")
    time.sleep(3)

    print("Form has been submitted successfully")
    time.sleep(10)

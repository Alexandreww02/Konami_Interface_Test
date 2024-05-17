from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_language(browser):
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("https://www.konami.com/games/silenthill/gate")

    time.sleep(3)

    try:

        cookie_element= browser.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie_element.click()
        time.sleep(3)

        select_language = browser.find_element(By.NAME,"selectRegion")
        select_language.click()
        time.sleep(2)

        select_english = browser.find_element(By.NAME,"selectRegion")
        select_english.send_keys("E"*2) 
        time.sleep(1)
      
        
        select_english.send_keys(Keys.RETURN)
        time.sleep(2)


        browser.close()
        
        
    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")


def test_birthday(browser):
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("https://www.konami.com/games/silenthill/gate")

    time.sleep(3)

    try:

        cookie_element= browser.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie_element.click()
        time.sleep(3)

        select_language = browser.find_element(By.NAME,"selectRegion")
        select_language.click()
        time.sleep(2)

        select_english = browser.find_element(By.NAME,"selectRegion")
        select_english.send_keys("E"*2) 
        time.sleep(1)
      
        
        select_english.send_keys(Keys.RETURN)
        time.sleep(2)

        select_month = browser.find_element(By.CLASS_NAME,"mm")
        select_month.send_keys("5")
        time.sleep(1)

        select_day = browser.find_element(By.CLASS_NAME,"dd")
        select_day.send_keys("3" * 2)
        time.sleep(1)

        select_year = browser.find_element(By.CLASS_NAME,"yyyy")
        select_year.send_keys("19")
        time.sleep(3)

        submit_button = browser.find_element(By.ID , "submit")
        submit_button.click()
        time.sleep(3)

        browser.close()
        
        
    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")

def test_youtube(browser):
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("https://www.konami.com/games/silenthill/gate")

    time.sleep(3)

    try:

        cookie_element= browser.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie_element.click()
        time.sleep(3)

        select_language = browser.find_element(By.NAME,"selectRegion")
        select_language.click()
        time.sleep(2)

        select_english = browser.find_element(By.NAME,"selectRegion")
        select_english.send_keys("E"*2) 
        time.sleep(1)
      
        
        select_english.send_keys(Keys.RETURN)
        time.sleep(2)

        select_month = browser.find_element(By.CLASS_NAME,"mm")
        select_month.send_keys("5")
        time.sleep(1)

        select_day = browser.find_element(By.CLASS_NAME,"dd")
        select_day.send_keys("3" * 2)
        time.sleep(1)

        select_year = browser.find_element(By.CLASS_NAME,"yyyy")
        select_year.send_keys("19")
        time.sleep(3)

        submit_button = browser.find_element(By.ID , "submit")
        submit_button.click()
        time.sleep(5)

        x_button = browser.find_element(By.XPATH , "/html/body/div[1]/div/nav/div/ul/li[1]/a")
        x_button.click()
        time.sleep(5)

        browser.close()
        
        
    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")




def test_steam():
        browser = webdriver.Chrome()
        browser.maximize_window()

        browser.get("https://www.konami.com/games/silenthill/gate")

        time.sleep(3)

        try:

            cookie_element= browser.find_element(By.ID, "onetrust-accept-btn-handler")
            cookie_element.click()
            time.sleep(3)

            select_language = browser.find_element(By.NAME,"selectRegion")
            select_language.click()
            time.sleep(2)

            select_english = browser.find_element(By.NAME,"selectRegion")
            select_english.send_keys("E"*2) 
            time.sleep(1)
        
            
            select_english.send_keys(Keys.RETURN)
            time.sleep(2)

            select_month = browser.find_element(By.CLASS_NAME,"mm")
            select_month.send_keys("5")
            time.sleep(1)

            select_day = browser.find_element(By.CLASS_NAME,"dd")
            select_day.send_keys("3" * 2)
            time.sleep(1)

            select_year = browser.find_element(By.CLASS_NAME,"yyyy")
            select_year.send_keys("19")
            time.sleep(3)

            submit_button = browser.find_element(By.ID , "submit")
            submit_button.click()
            time.sleep(3)

            scroll = browser.execute_script("window.scrollTo(0 , 1500);")
            time.sleep(3)

            steam_redirect = browser.find_element(By.XPATH,"/html/body/div[1]/div/section[4]/div[2]/ul/li[2]/div/div[3]/div/ul/li[2]/a")
            steam_redirect.click()
            time.sleep(5)

            browser.close()
            
            
        except Exception as e:
            pytest.fail(f"Testul a eșuat cu eroarea: {e}")
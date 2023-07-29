import time
from datetime import date
from time import strptime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument("--disable-gpu")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def scrape():

    simplepractice_data_list = []
    driver = webdriver.Chrome(options=options)
    # get simplepractice.com
    driver.get("https://secure.simplepractice.com/users/sign_in")
    print("sdfdfd")
    # get login id element
    login_id= driver.find_element(By.NAME,"user[login]")
    login_id.send_keys("nuphysical.info@gmail.com")
    # get login password element
    login_password = driver.find_element(By.NAME,"user[password]")
    login_password.send_keys("Frohliche23#")
    # get login button element
    login_button = driver.find_element(By.NAME,"commit")
    login_button.click()
    try:
        wait = WebDriverWait(driver, 10)
        # skip welcome page
        try:
            skip_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[button/@class ='button ghost']")))
            skip_element.click()
        except:
            pass
        client_element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Clients")))
        client_element.click()
        manage_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[button/@class ='button-link options']")))
        for manage in manage_elements:
            manage.click()
            time.sleep(3)
            href_element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Edit Client info"))).get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(href_element)
            email= wait.until(EC.presence_of_element_located((By.NAME,'email'))).get_attribute('value')
            first_name= wait.until(EC.presence_of_element_located((By.ID,'firstName'))).get_attribute('value')
            last_name= wait.until(EC.presence_of_element_located((By.ID,'lastName'))).get_attribute('value')
            month = driver.find_element(By.NAME, 'month').get_attribute('value')
            day = driver.find_element(By.NAME, 'day').get_attribute('value')
            year = driver.find_element(By.NAME, 'year').get_attribute('value')
            if month=='MM' and day=='DD' and year=='YYYY':
                age= None
                dob = None
            else:
                age= calculateAge(date(int(year),strptime(month,'%B').tm_mon,int(day)))
                dob=year+"-"+str(strptime(month,'%B').tm_mon)+"-"+day
            try:
                phone_number= wait.until(EC.presence_of_element_located((By.NAME,'phone'))).get_attribute('value')
            except:
                phone_number = None
                simplepractice_data_list.append({"email":email,"firstName":first_name,"lastName":last_name,"phone":phone_number,"age":age,"dob":dob})
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(3)
                manage.click()
                continue
            simplepractice_data_list.append({"email":email,"firstName":first_name,"lastName":last_name,"phone":phone_number,"age":age,"dob":dob})
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
            manage.click()
    except:
        pass
    return simplepractice_data_list

print("Done")



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from time import sleep
from sys import exit

from database_class import Database

class Car_bot:
    def __init__(self,domain,dbname,delay):
        self.browser = webdriver.Firefox(executable_path="geckodriver")
        self.domain = domain
        self.delay = delay
        self.dbname = dbname

    def login(self,username,password):
        self.browser.get(self.domain)
        try:
            login_button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'auth0-lock-submit')))
            username_input = self.browser.find_element_by_id("1-email")
            password_input = self.browser.find_element_by_name("password")
            username_input.send_keys(username)
            password_input.send_keys(password)
            login_button.click()
            sleep(5)
        except TimeoutException:
            print("Can't lacate login button")
            exit()
        except:
            print("Something went wrong")
            exit()
    #choose picup or delivery by filter id
    def select_jobs(self,state,filter_id):
        db = Database(self.dbname)
        while True:
            blacklisted = True
            try:
                self.browser.get(self.domain)
                wait = WebDriverWait(self.browser,10)
                delivery_select = Select(wait.until(EC.visibility_of_element_located((By.ID, filter_id))))
                delivery_select.select_by_visible_text(state)
                filter_button = self.browser.find_element_by_id("Filter")
                filter_button.click()
                select_jobs_button = wait.until(EC.visibility_of_element_located((By.ID, "Submit")))

                rowheight = self.browser.find_elements_by_class_name("rowheight")
                for each in rowheight:
                    td = each.find_elements_by_tag_name("td")
                    checkboxes = td[0].find_elements_by_tag_name("input")
                    order_id = td[1].text
                    check_in_db = db.check_order_id(order_id)
                    if check_in_db == 0:
                        checkboxes[1].click()
                        db.insert(order_id)
                        blacklisted = False
                if len(rowheight) == 0:
                    print("Nothing to select!!!")
                elif blacklisted:
                    print("Only blacklisted items!!!")

                select_jobs_button.click()
            except TimeoutException:
                print("Error: Can't lacate element")
            except:
                print("Error: Something went wrong")


            sleep(self.delay)

    def select_jobs_mixed(self,p_state,d_states):
        db = Database(self.dbname)
        while True:
            blacklisted = True
            try:

                self.browser.get(self.domain)
                wait = WebDriverWait(self.browser,10)
                delivery_select = Select(wait.until(EC.visibility_of_element_located((By.ID, "p_filter"))))
                delivery_select.select_by_visible_text(p_state)
                filter_button = self.browser.find_element_by_id("Filter")
                filter_button.click()
                select_jobs_button = wait.until(EC.visibility_of_element_located((By.ID, "Submit")))

                rowheight = self.browser.find_elements_by_class_name("rowheight")
                for each in rowheight:
                    td = each.find_elements_by_tag_name("td")
                    if td[11].text.strip() in d_states:
                        checkboxes = td[0].find_elements_by_tag_name("input")
                        order_id = td[1].text
                        check_in_db = db.check_order_id(order_id)
                        if check_in_db == 0:
                            checkboxes[1].click()
                            db.insert(order_id)
                            blacklisted = False
                if len(rowheight) == 0:
                    print("Nothing to select!!!")
                elif blacklisted:
                    print("Only blacklisted items!!!")

                select_jobs_button.click()

            except TimeoutException:
                print("Error: Can't locate element")

            except:
                print("Error: Something went wrong")

            sleep(self.delay)
    def __del__(self):
        self.browser.close()


#askldjailwijaliwdilajslkdjaksjdioawjdlaksnlkasndojas

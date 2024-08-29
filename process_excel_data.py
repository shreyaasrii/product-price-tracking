import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from excel_file_creator import ExcelFileCreator
from send_mail import EmailSender

amazon_xpaths = ['/html/body/div[4]/div/div[3]/div[11]/div[17]/div/div/div[4]/div[1]/span[3]/span[2]/span[2]',
                 '/html/body/div[2]/div/div[5]/div[3]/div[4]/div[14]/div/div/div[4]/div[1]/span[3]/span[2]/span[2]']

class ProcessExcelData:
    def __init__(self, data):
        self.data = data

    def getElement(self, xpath, driver):
        try:
            element = driver.find_element(By.XPATH, xpath)
            return element.text
        except:
            return None

    def get_mail_data(self, ele, int_data):
        subject = """Alert : Price for '{}' product is dropped :- {}""".format(ele['Item'], int_data)
        body = """Hi,\n\nPrice for '{}' product is dropped :- {}, Hurry!!!\n\nThanks,\nTeam Support""".format(ele['Item'], int_data)
        return (subject, body)

    def process_data(self):
        chromedriver_path = '/usr/local/bin/chromedriver'
        service = ChromeService(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service)
        for ele in self.data:
            url = ele['Url']
            driver.get(url)
            print(driver.title)

            data = None
            for xpath in amazon_xpaths:
                data = self.getElement(xpath, driver)
                if data != None:
                    break
        
            if data != None:
                data = data.replace(",", "").strip()
                int_data = int(data)
                if ele['Threshold_Amount'] > int_data :
                    ele['Status'] = """Price for this product dropped :- {}""".format(int_data)
                    (subject, body) = self.get_mail_data(ele, int_data)
                    EmailSender().send_mail(subject, body, ele['Notify_Email_Ids'])
                else:
                    ele['Status'] = """Price for this product is not dropped :- {}""".format(int_data)
            else:
                ele['Status'] = 'ERROR: Data is not able to process for this, due to some technical error'

        driver.quit()
        creator = ExcelFileCreator(self.data)
        creator.create_file_with_data()



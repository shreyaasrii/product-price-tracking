import warnings
import pandas as pd
import logging

warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')

from read_online_tracker_data import ReadOnlineTracker
from process_excel_data import ProcessExcelData

def main():
    logger = logging.getLogger(__name__)
    data = ReadOnlineTracker().read()
    logger.info("""Data got - {}""".format(data))
    ProcessExcelData(data).process_data()

def getElement(xpath, driver):
	try:
		element = driver.find_element(By.XPATH, xpath)
		return element.text
	except:
		return None

if __name__ == "__main__":
    main()





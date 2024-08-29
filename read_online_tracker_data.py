import pandas as pd

file_path = '<file_path>/Online_Tracker_File.xlsx'
sheet_name = 'Data'

class ReadOnlineTracker:
    def __init__(self):
        self.file_path = file_path
        self.sheet_name = sheet_name

    def read(self):
    	data = []
    	df = pd.read_excel(self.file_path, sheet_name=self.sheet_name, engine='openpyxl')

    	for row in df.itertuples(index= False, name = None):
    		(Sr_No, Item, Url, Threshold_Amount, Notify_Email_Ids) = row
    		tmp_dict = {}
    		tmp_dict['Sr_No'] = Sr_No
    		tmp_dict['Item'] = Item
    		tmp_dict['Url'] = Url
    		tmp_dict['Threshold_Amount'] = Threshold_Amount
    		tmp_dict['Notify_Email_Ids'] = Notify_Email_Ids
    		data.append(tmp_dict)
    	return data

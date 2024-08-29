import pandas as pd

file_path = '<file_path>/Result_Online_Tracker_File_With_Data.xlsx'

class ExcelFileCreator:
    def __init__(self, data):
        self.file_path = file_path
        self.data = data

    def create_file_with_data(self):
        df = pd.DataFrame(self.data)
        df.to_excel(self.file_path, sheet_name='Data', index=False)

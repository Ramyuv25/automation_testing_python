import openpyxl
class Excel_reader:
    def __init__(self,file_path):
        self.file_path = file_path
        self.workbook=openpyxl.load_workbook(self.file_path)
       # self.sheet=self.workbook.get_sheet_by_name('Sheet1')
        self.sheet=self.workbook.active

    def get_row_data(self,row_number):

        data={}
        headers=[cell.value for cell in self.sheet[1]]
        row=[cell.value for cell in self.sheet[row_number]]
        for header,value in zip(headers,row):
            data[header]=str(value)
        return data


    def get_all_rows(self):
        rows=[]
        for row in range(2,self.sheet.max_row+1):
            rows.append(self.get_row_data(row))
        return rows
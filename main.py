import pandas as pd
import os
import glob

os.getcwd()
os.chdir('data')
print(os.getcwd())

xl_files = glob.glob('*.xlsx')
print(xl_files)

combined = pd.DataFrame()

for xl_file in xl_files:
    # Создать объект ExcelFile
    xl_file_obj = pd.ExcelFile(xl_file)
    # Цикл по листам
    for sheet_name in xl_file_obj.sheet_names:
        # Прочитать нужный лист книги
        data = pd.read_excel(xl_file_obj, sheet_name=sheet_name)
        # Дописать в датафрейм combined
        combined = combined._append(data)

combined.to_excel('sales_combined.xlsx', index=False)
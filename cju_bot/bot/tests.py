from django.test import TestCase
from datetime import datetime 
import pandas as pd
# Create your tests here.

filename = 'text.xlsx'
sheet_name = 'Sheet1'
book = pd.read_excel(filename, sheetname=sheet_name, header=1) # 헤더 설정 가능

book = book.sort_value(by=2019, ascending=False) # 정렬 적용
print(book)
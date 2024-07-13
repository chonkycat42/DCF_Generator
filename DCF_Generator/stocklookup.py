import pandas as pd
import yfinance as yf
import openpyxl
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os





def stock_lookup(company):
    stock = company

    #info = yf.Ticker(company).history(
        #period='1mo',
        #interval='1d')
    

    #if len(info) <= 0:
        #return 'error'


    comp = yf.Ticker(stock)
    
    
    

    # Free Cash Flows
    data = []
    for i in range(0,3):
        data.append(comp.cashflow.loc['Free Cash Flow'][i])
        
        
    
        



    year_2021 = data[-1]
    year_2022 = data[-2]
    year_2023 = data[-3]

    # The other stuff
    #for key,value in comp.balance_sheet.items():
        #print(key,":",value)

    shares_outstanding = comp.info['sharesOutstanding']
    total_debt = comp.info['totalDebt']

    cash_equvalents = comp.balance_sheet.loc['Cash And Cash Equivalents'][0]


    replacement_list = {
        "[Stock Name]": stock.upper(),
        "X1": year_2021,
        "X2": year_2022,
        "X3": year_2023,
        "X4": cash_equvalents,
        "X5": total_debt,
        "X6": shares_outstanding


    }

    wb = openpyxl.load_workbook("DCFTemplate.xlsx")

    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if cell.value in replacement_list.keys():
                    cell.value = replacement_list.get(cell.value)



    dir_name = filedialog.askdirectory()
    
    
    wb.save(dir_name+"\\"+"DCF of "+stock.upper()+".xlsx")
    return 



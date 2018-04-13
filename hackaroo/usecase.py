import xlrd
import numpy as np
DATA_FILE='data/Fire_Theft.xls'
# Step 1: read in data from the .xls file
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1
for col in range(sheet.ncols):
    print(sheet.cell_value(0,col))
for col in range(sheet.ncols):
    print(sheet.cell_value(1,col))

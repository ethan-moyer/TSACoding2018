import xlrd
book = xlrd.open_workbook('R8_2018_HS_Coding.xls')
values = book.sheet_by_index(0)
velocity = []
#For loop is to calculate velocity. Prints every given velocity.
for i in range(1, values.nrows):
    velocity.append((values.cell(i,1).value)/(values.cell(i,0).value))
    print(velocity[i-1])
print(values.nrows)

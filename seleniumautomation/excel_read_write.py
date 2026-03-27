import openpyxl

excel_book = openpyxl.load_workbook("pyexcel.xlsx")
active_sheet = excel_book.active
cell_value_header = active_sheet.cell(row=1, column=1).value
cell_value = active_sheet.cell(row=2, column=2).value
print('Header values', cell_value_header)
print('Row values', cell_value)

print('Max row in sheet', active_sheet.max_row)
print('Max column in sheet', active_sheet.max_column)

# excel_book.save("pyexcel.xlsx")
Dict_names = {}
# Loop it up and print all the values
for i in range(1, active_sheet.max_row + 1):
    if active_sheet.cell(row=i, column=1).value == "Test case 2 ":
        for j in range(2, active_sheet.max_column + 1):
            print(active_sheet.cell(row=i, column=j).value)
            # append the values to a dict
            Dict_names[active_sheet.cell(row=1, column=j).value] = active_sheet.cell(row=i, column=j).value

print(Dict_names)
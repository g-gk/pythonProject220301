import xlsxwriter
from sys import stdin

data = []
for s in stdin:
    data.append(s.split('\n')[0].split())

workbook = xlsxwriter.Workbook('res.xlsx')
worksheet = workbook.add_worksheet()
row = 0
for item in data:
    worksheet.write(row, 0, item[0])
    worksheet.write(row, 1, int(item[1]))
    row += 1

chart1 = workbook.add_chart({'type': 'pie'})
chart1.add_series({

    'name': '',

    'categories': ['Sheet1', 0, 0, row - 1, 0],

    'values': ['Sheet1', 0, 1, row - 1, 1],
})
worksheet.insert_chart('C2', chart1, {'x_offset': 25, 'y_offset': 10})

workbook.close()

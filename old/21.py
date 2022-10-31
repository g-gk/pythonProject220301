from xlsxwriter import Workbook
from sys import stdin

workbook = Workbook('res.xlsx')
worksheet = workbook.add_worksheet()

data = list(map(str.strip, stdin))
data1 = []
for i in data:
    i = i.split()
    i = (i[0], int(i[1]))
    data1.append(i)

for row, (item, price) in enumerate(data1):
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, price)

chart = workbook.add_chart({'type': 'pie'})
chart.add_series({'values': '=Sheet1!B1:{0}'.format('B' + str(len(data1)))})
worksheet.insert_chart('C3', chart)

workbook.close()

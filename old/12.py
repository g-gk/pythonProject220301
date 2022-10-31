import xlsxwriter
import sys

workbook = xlsxwriter.Workbook('res.xlsx')
worksheet = workbook.add_worksheet()

data = sys.stdin.read().split('\n')
data = list(map(str.strip, data))

for i in data:
    i = i.split()
    i = (i[0], int(i[1]))
    data.append(i)

for row, (item, price) in enumerate(data):
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, price)

chart = workbook.add_chart({'type': 'pie'})
chart.add_series({'values': '=Sheet1!B1:{0}'.format('B' + str(len(data)))})
worksheet.insert_chart('C3', chart)
workbook.close()

import xlsxwriter
import sys

data = sys.stdin.readlines()
a = []
for i in data:
    i = i[:-1]
    b = i.split()
    b[1] = int(b[1])
    a.append(b)
workbook = xlsxwriter.Workbook('res.xlsx')
worksheet = workbook.add_worksheet()

for row, (item, price) in enumerate(a):
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, price)

chart = workbook.add_chart({'type': 'pie'})
a = '=Sheet1!B1:B' + str(len(a))

chart.add_series({'values': a, 'categories': '=Sheet1!A1:{0}'.format('A' + str(len(data)))})

worksheet.insert_chart('C3', chart)
workbook.close()

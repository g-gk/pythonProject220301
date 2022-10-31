import xlsxwriter
import sys

workbook = xlsxwriter.Workbook("test.xlsx")

worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': 1})

pokupki = []
cena = []
cenas = []
cenaa = []

d = list(map(str.strip, sys.stdin))

for x in d:
    x = x.split()
    pokupki.append(x[0])
    cenas.append(int(x[1]))
    cenaa.append(int(x[1]))

last_row = len(d)

cenas = sum(cenas)

for i in range(len(cenaa)):
    print(cenaa[i] / cenas)
    cena.append(cenaa[i])

print(cenas, cenaa, cena)
# headings = ['Category', 'Values']

data = [

    pokupki,
    cena,
    #    ['Apple', 'Cherry', 'Banana'],
    #    [50, 40, 10],

]

# worksheet.write_row('A1', headings, bold)

worksheet.write_column('A1', data[0])
worksheet.write_column('B1', data[1])

chart1 = workbook.add_chart({'type': 'pie'})

chart1.add_series({
    'name': '',
    'categories': ['Sheet1', 0, 0, last_row - 1, 0],
    'values': ['Sheet1', 0, 1, last_row - 1, 1],

})

chart1.set_style(10)

worksheet.insert_chart('C2', chart1, {'x_offset': 25, 'y_offset': 10})

workbook.close()

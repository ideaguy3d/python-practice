import xlsxwriter

data = '../data/'


def create_hello_world():
    workbook = xlsxwriter.Workbook(data + 'hello_excel-1.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Hello world')
    workbook.close()
    pass  # def create_hello_world():


def simple_xlsx():
    workbook = xlsxwriter.Workbook(data + 'Expenses01.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    money = workbook.add_format({'num_format': '$#,##0'})
    fill = workbook.add_format({'bg_color': 'green'})
    worksheet.write('A1', 'Item', bold)
    worksheet.write('B1', 'Cost', bold)
    expenses = (
        ['Rent', 1000],
        ['Gas', 100],
        ['Food', 300],
        ['Gym', 50],
    )
    row = 1  # start at 1
    col = 0
    for item, cost in expenses:
        worksheet.write(row, col, item)
        if row % 2 == 0:
            worksheet.write(row, col+1, cost, fill)
        else:
            worksheet.write(row, col + 1, cost, money)
        row += 1
    worksheet.write(row, 0, 'Total', bold)
    worksheet.write(row, 1, '=sum(b1:b4)', money)
    workbook.close()
    pass  # def create_hello_world():


simple_xlsx()

# end of file

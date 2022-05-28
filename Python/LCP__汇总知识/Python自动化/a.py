import xlwings as xw
app = xw.App(visible = True, add_book = False)
workbook = app.books.add()
workbook.save(".\\新文件.xlsx")

workbook.close()
app.quit()



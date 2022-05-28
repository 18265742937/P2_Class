import xlwings as xw
app = xw.App(visible = True, add_book = False)
for i in range(1, 21):
    workbook = app.books.add()
    workbook.save(f'.\\新文件{i}.xlsx')
    workbook.close()
app.quit()





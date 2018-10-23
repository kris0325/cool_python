import xlwt


def writerExcel():
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('My Worksheet')
    worksheet.write(0, 0, label = 'P42836202.0_I155207111.0')
    workbook.save('Excel_Workbook.xls')


def main():
      writerExcel()
      # csvfile.close()

if __name__=="__main__":
        main()

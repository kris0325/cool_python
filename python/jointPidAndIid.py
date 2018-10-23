# -*- coding: utf-8 -*-
import  xdrlib ,sys
import xlrd
import csv
import xlwt

csvfile = file('csv_test.csv', 'wb')
writer = csv.writer(csvfile)

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')

def open_excel(file= 'file.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)




#join col by "-"
def join_clo(file= 'file.xlsx',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据



    joinstr = '_'
    lists = []
    for i in range(0,nrows):
             newcell = 'P'+ str(table.cell_value(i,0)) + '_'+ 'I'+ str(table.cell_value(i,1))
             print newcell
             #writer.writerow(newcell)
             worksheet.write(0, i, label = newcell)

def main():
  join_clo()
  csvfile.close()
  workbook.save('Excel_Workbook.xls')


if __name__=="__main__":
    main()

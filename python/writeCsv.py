


# -*- coding: utf-8 -*-
import  xdrlib ,sys
import xlrd
import csv

csvfile = file('csv_test.csv', 'wb')
writer = csv.writer(csvfile)


def writerCsv():
    writer.writerow(P58666244_I203500366)


def main():
  writerCsv()
  csvfile.close()

if __name__=="__main__":
    main()

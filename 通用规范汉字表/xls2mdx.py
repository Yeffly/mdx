# 通用规范汉字表.xls _from_ https://github.com/bedlate/cn-corpus/blob/master/通用规范汉字表.xls
# writedict _from_ https://github.com/skywind3000/writemdict

from __future__ import unicode_literals
import os, xlrd
from writemdict import MDictWriter

def main():
    py_location = os.path.dirname(os.path.abspath(__file__))
    print(py_location) # 打印当前 py 文件所在目录
    workbook = xlrd.open_workbook(os.path.join(py_location,r"通用规范汉字表.xls"))
    dictionary = {}
    for sheet in workbook.sheets():
        for row in range(sheet.nrows):
            zi_tou = sheet.cell(row, 1).value
            xu_hao = str(int(sheet.cell(row, 0).value)).zfill(4)
            print(sheet.name, xu_hao, zi_tou)
            #f.write(zi_tou + '\t' + xu_hao + '\t' + sheet.name + '\n')
            dictionary[zi_tou] = '<b>' + zi_tou + '</b>' + '\t' + xu_hao + '\t' + sheet.name

    writer = MDictWriter(dictionary, title="", description="")
    outfile = open(os.path.join(py_location,r"通用规范汉字表.mdx"), "wb")
    writer.write(outfile)
    outfile.close()

    print('done!')


if __name__ == "__main__":
    main()
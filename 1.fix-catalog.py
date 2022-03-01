
import csv
import codecs
import xlrd

def csvload(src,srccoding='utf-8',dem=',',ignoreMark=None):
    f = open(src, "r", encoding=srccoding)
    reader = csv.reader(f,delimiter=dem)
    lis = list(reader)
    if ignoreMark:
        for it in lis:
            if it[0].startswith(ignoreMark):
                lis.remove(it)
    return lis

def csvdump(dic,dst,srccoding='utf-8-sig',dem=','):
    with codecs.open(dst, 'w', encoding=srccoding) as f:
        write = csv.writer(f,delimiter=dem)
        write.writerows(dic)
    f.close()

xlsx = xlrd.open_workbook('stellarium-fix.xls')
sheet1 = xlsx.sheets()[0]
vmaglis={}
for i in range(1,sheet1.nrows):
    vmaglis[str(int(sheet1.row(i)[0].value))]=sheet1.row(i)[2].value
sheet2 = xlsx.sheets()[1]
poslis={}
for i in range(1,sheet2.nrows):
    poslis[str(int(sheet2.row(i)[0].value))]=[sheet2.row(i)[2].value,sheet2.row(i)[3].value]


if __name__=='__main__':
    lis=csvload("catalog.txt",'utf-8-sig','\t')
    for i in range(len(lis)):
        if str(lis[i][0]) in vmaglis:
            lis[i][4]=vmaglis[str(lis[i][0])]

        if str(lis[i][0]) in poslis:
            lis[i][1]=poslis[str(lis[i][0])][0]
            lis[i][2]=poslis[str(lis[i][0])][1]

    csvdump(lis,"catalog1.txt",'u8',dem='\t')

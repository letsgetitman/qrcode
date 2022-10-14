import openpyxl
import xlrd
import pandas as pd
import qrcode
import pprint

QR = qrcode.QRCode()
QR2 = qrcode.QRCode()


wb = openpyxl.load_workbook('breast_cancer.xlsx')
ws = wb.active



for i in range(1,3):
    QR.clear()
    for row in ws[i]:
        print(row.value)
        QR.add_data(row.value)
        QR.add_data(",")
    Gen_Qr = QR.make_image(fill_color = "red", black_color = "black")
    Gen_Qr.save("qr{}.jpg".format(i))
        




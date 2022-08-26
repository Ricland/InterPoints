import sys
from PyQt5 import QtWidgets, QtGui
import design
import math

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Form) :
    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.solve) #нажатие на кнопку
 
    def solve (self) :
        self.textEdit.clear()
        lat1 = self.lineEdit.text()
        lng1 = self.lineEdit_2.text()
        lat2 = self.lineEdit_3.text()
        lng2 = self.lineEdit_4.text()
        n = self.lineEdit_5.text()

        if validation_of_data (lat1, lng1, lat2, lng2, n) : 
            lat1 = degToRad(float(self.lineEdit.text()))
            lng1 = degToRad(float(self.lineEdit_2.text()))
            lat2 = degToRad(float(self.lineEdit_3.text()))
            lng2 = degToRad(float(self.lineEdit_4.text()))
            n = abs(int(self.lineEdit_5.text()))
            f0 = 1 / (n + 1)
            f = f0
            rlat = lat1
            rlng = lng1
            d = 2 * math.asin(math.sqrt((math.sin((lat1 - lat2) / 2)) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lng1 - lng2) / 2) ** 2))
            self.textEdit.insertPlainText("Расстояние между начальной и конечной точками: " + '{:.3f}'.format(d * 6371) + "\n\n")

            for i in range(1, n + 1) : 
                A = math.sin((1 - f) * d) / math.sin(d)
                B = math.sin(f * d) / math.sin(d)
                x = A * math.cos(lat1) * math.cos(lng1) + B * math.cos(lat2) * math.cos(lng2)
                y = A * math.cos(lat1) * math.sin(lng1) + B * math.cos(lat2) * math.sin(lng2)
                z = A * math.sin(lat1) + B * math.sin(lat2)
                lat = math.atan2(z, math.sqrt(x ** 2 + y ** 2))
                lng = math.atan2(y, x)
                dr = 12742 * math.asin(math.sqrt((math.sin((rlat - lat) / 2)) ** 2 + math.cos(rlat) * math.cos(lat) * math.sin((rlng - lng) / 2) ** 2))
                self.textEdit.insertPlainText('{:.5f}'.format(radToDeg(lat)) + '    ' + '{:.5f}'.format(radToDeg(lng)) + ' \tdr = ' + '{:.3f}'.format(dr) + "\n")
                rlat = lat
                rlng = lng
                f += f0
        else :
            self.textEdit.insertPlainText("Ошибка ввода!")
 
def degToRad (a) : 
    return a * math.pi / 180.

def radToDeg (a) :  
    return a * 180. / math.pi

def validation_of_data (lat1, lng1, lat2, lng2, n) :
    try :
        float(lat1)
        float(lng1)
        float(lat2)
        float(lng2)
        int(n)
        return True
    except Exception :
        return False
        
def main() :
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__' :
    main()

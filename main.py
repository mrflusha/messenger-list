import sys
import info_box
import func
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QComboBox, QAction, QTabWidget, QVBoxLayout, QInputDialog, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):


    def __init__(self):
        super().__init__()
        self.title = 'Messenger list'
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 400
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Сrash 2020.')

        
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
    
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(100,50)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Вывод из базы")
        self.tabs.addTab(self.tab2,"Добавить в базу")
        self.tabs.addTab(self.tab3,"Удаление из базы")
        self.tabs.addTab(self.tab4,"Сортировка мессенджеров")
        
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)



        self.dblist = QComboBox()
        self.dblist.setObjectName("dblist")

        func.getCombolist(self.dblist, func.connectdb.array)
        self.pushEdit = QPushButton("Вывод из базы")
        self.tab1.layout.addWidget(self.dblist)
        self.tab1.layout.addWidget(self.pushEdit)
        self.tab1.setLayout(self.tab1.layout)

        self.pushEdit.clicked.connect(self.import_click)
        
        #SECOND TAB 
        self.tab2.layout = QVBoxLayout(self)
        self.title = QLabel("Введите название мессенджера:")
        self.title_manuf = QLabel("Введите Производителя:")
        self.addMaxSize = QComboBox()
        func.getCombolist(self.addMaxSize , func.connectdb.maxsize)
        self.addSupportVC = QComboBox()
        func.getCombolist(self.addSupportVC , func.connectdb.oneOrZero)
        self.addSupportOS = QComboBox()
        func.getCombolist(self.addSupportOS , func.connectdb.operatingSyS)
        self.addSupportVM = QComboBox()
        func.getCombolist(self.addSupportVM , func.connectdb.oneOrZero)
        self.addSupportGC = QComboBox()
        func.getCombolist(self.addSupportGC , func.connectdb.oneOrZero)
        self.addMaxFileSize = QLabel()
        self.addVC = QLabel()
        self.addOS = QLabel()
        self.addVM = QLabel()
        self.addGC = QLabel()
        self.textbox = QLineEdit(self)
        self.textbox_title = QLineEdit(self)


        
        #func.yesorno(self.addSupportVC, "YES")


        self.addMaxFileSize.setText("Максимальный размер файла:")
        self.addVC.setText("Видеовызов:")
        print(self.addSupportVC)
        self.addOS.setText("Поддерживаемые ОС:")
        self.addVM.setText("Голосовые сообжения:")
        self.addGC.setText("Поддержка групповых чатов:")
        self.pushAdd = QPushButton("Добавить в базу")

        self.tab2.layout.addWidget(self.title)
        self.tab2.layout.addWidget(self.textbox)
        self.tab2.layout.addWidget(self.title_manuf)
        self.tab2.layout.addWidget(self.textbox_title)
        self.tab2.layout.addWidget(self.addVC)
        self.tab2.layout.addWidget(self.addSupportVC)
        self.tab2.layout.addWidget(self.addGC)
        self.tab2.layout.addWidget(self.addSupportGC)
        self.tab2.layout.addWidget(self.addVM)
        self.tab2.layout.addWidget(self.addSupportVM)
        self.tab2.layout.addWidget(self.addOS)
        self.tab2.layout.addWidget(self.addSupportOS)
        self.tab2.layout.addWidget(self.addMaxFileSize)
        self.tab2.layout.addWidget(self.addMaxSize)
        self.tab2.layout.addWidget(self.pushAdd)
        self.tab2.setLayout(self.tab2.layout)
        #Button call
        self.pushAdd.clicked.connect(self.add_click)


        #THIRD TAB

        self.tab3.layout = QVBoxLayout(self)


        self.deletebox=QComboBox()

        func.getCombo(self.deletebox)



        self.tab3.layout.addWidget(self.deletebox)






        self.pushDelete = QPushButton("Удаление из базы")




        self.tab3.layout.addWidget(self.pushDelete)
        self.tab3.setLayout(self.tab3.layout)



        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


        self.pushDelete.clicked.connect(self.delete_click)








        #4th tab:
        self.tab4.layout = QVBoxLayout(self)
        self.title = QLabel("Выбор по функциональности:\n")
        self.filterFileSize = QComboBox()
        func.getCombolist(self.filterFileSize , func.connectdb.maxsize)
        self.filterSupportVC = QComboBox()
        func.getCombolist(self.filterSupportVC , func.connectdb.oneOrZero)
        self.filterSupOS = QComboBox()
        func.getCombolist(self.filterSupOS , func.connectdb.operatingSyS)
        self.filterSupVM = QComboBox()
        func.getCombolist(self.filterSupVM , func.connectdb.oneOrZero)
        self.filterSupGC = QComboBox()
        func.getCombolist(self.filterSupGC , func.connectdb.oneOrZero)
        self.filterMaxFileSize = QLabel()
        self.filterVC = QLabel()
        self.filterOS = QLabel()
        self.filterVM = QLabel()
        self.filterGC = QLabel()



        self.filterMaxFileSize.setText("Максимальный размер файла:")
        self.filterVC.setText("Видеовызов:")
        print(self.filterSupportVC)
        self.filterOS.setText("Поддерживаемые ОС:")
        self.filterVM.setText("Голосовые сообщения:")
        self.filterGC.setText("Поддержка групповых чатов:")
        self.execDB = QPushButton("Фильтрация")



        self.tab4.layout.addWidget(self.title)
#        self.tab4.layout.addWidget(self.textbox) 
        self.tab4.layout.addWidget(self.filterVC)
        self.tab4.layout.addWidget(self.filterSupportVC)
        self.tab4.layout.addWidget(self.filterGC)
        self.tab4.layout.addWidget(self.filterSupGC)
        self.tab4.layout.addWidget(self.filterVM)
        self.tab4.layout.addWidget(self.filterSupVM)
        self.tab4.layout.addWidget(self.filterOS)
        self.tab4.layout.addWidget(self.filterSupOS)
        self.tab4.layout.addWidget(self.filterMaxFileSize)
        self.tab4.layout.addWidget(self.filterFileSize)
        self.tab4.layout.addWidget(self.execDB)
        self.tab4.setLayout(self.tab4.layout)





        
    @pyqtSlot()
    def delete_click(self):





        print(self.deletebox.currentIndex())
        buttonreply = QMessageBox.question(self, 'Уведомление', "Вы действительно хотите удалить из базы?", QMessageBox.Yes | QMessageBox.Abort)
        if buttonreply == QMessageBox.Yes:
            delete_title = self.deletebox.currentText()
            delete_id = self.deletebox.currentIndex()
            print (delete_title)

            func.connectdb.del_db("all_messengers",delete_title)

            print("YES")
            QMessageBox.information(self, "Уведомление", str(delete_title)+"\nУдалён из базы данных" , QMessageBox.Ok)
        elif buttonreply == QMessageBox.Abort:
            QMessageBox.warning(self, "Cancel", "Действие отменено", QMessageBox.Abort)   
    def add_click(self):
        textboxValue = self.textbox.text()
        self.textbox.setText("BULL") 
        index_arr = (textboxValue, self.textbox_title.text(), self.addMaxSize.currentIndex(),self.addSupportOS.currentIndex(),self.addSupportVM.currentIndex(),self.addSupportGC.currentIndex(),self.addSupportVC.currentIndex())
        index_str = ""

        



        buttonreply = QMessageBox.question(self, 'Уведомление', "Вы действительно хотите добавить в базу?", QMessageBox.Yes | QMessageBox.Abort)
        if buttonreply == QMessageBox.Yes:
            info_box.insert_db(str(index_arr),index_arr[1])
            print(self.addMaxSize.currentIndex())
            add_index=[self.addMaxSize.currentIndex(),self.addSupportOS.currentIndex()]
            print (add_index)
            io = self.addSupportOS.currentText()

            print("YES")
            self.dblist.clear()
            func.getCombolist(self.dblist, func.connectdb.array)
            QMessageBox.information(self, "Уведомление", str(io)+"\nИндекс" , QMessageBox.Ok)
        elif buttonreply == QMessageBox.Abort:
            QMessageBox.warning(self, "Cancel", "Действие отменено", QMessageBox.Abort)
    def import_click(self):

#Index of messenger title
        import_index = self.dblist.currentIndex()
        import_name = self.dblist.currentText()
        bd_array =[]

        info_box.max_upload(import_name,bd_array)
        
      


        import_up = func.connectdb.maxsize[bd_array[0][0]]
        import_gv = func.connectdb.oneOrZero[bd_array[0][1]]
        import_vm = func.connectdb.oneOrZero[bd_array[0][2]]
        import_vv = func.connectdb.oneOrZero[bd_array[0][3]]
        import_os = func.connectdb.operatingSyS[bd_array[0][4]]
        import_manufact = func.connectdb.manufact[bd_array[0][5]]
        print(import_up)
        print(import_gv)
        print(import_vm)
        print(import_vv)
        



#Get import string
        #import_manufact = func.connectdb.manufact[import_index]
        #import_str = str("\nПроизводитель: " + import_name + "\nМаксимальный размер файла: " )




        
        #print (import_index,import_name,import_manufact,"\n", import_str)
        

#        zaglushka = str(func.connectdb.result[0])+"\n"+str(func.connectdb.manufact[0])+"\n"+str(func.connectdb.oneOrZero[0])

        buttonreply = QMessageBox.information(self, "Info about "+ import_name,"Название:\t\t\t"+ import_name + "\nПроизводитель: \t\t" +import_manufact+ "\nМаксимальный размер файла: \t" + import_up +"\nПоддержка групповых чатов:\t"+import_gv+"\nПоддержка групповых сообщений:\t"+import_vm+"\nПоддержка Видеовызова:\t"+import_vv+"\nПоддерживаемы ОС: \t\t"+import_os , QMessageBox.Ok)
#this func may be will need
        #for currentQTableWidgetItem in self.tableWidget.selectedItems():
            #print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

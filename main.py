import sys
import info_box
import func
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QComboBox, QAction, QTabWidget, QVBoxLayout, QInputDialog, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot
from time import sleep as freeze



class App(QMainWindow):


    def __init__(self):
        super().__init__()
        self.title = 'Messenger list'
        self.left = 300
        self.top = 15
        self.width = 600
        self.height = 680
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('2020.')

        try:
            self.table_widget = MyTableWidget(self)
        except:
            QMessageBox.warning(self, 'Connection status',"ERROR:\nBad connection\n", QMessageBox.Ok)
            sys.exit()
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
        self.tabs.resize(50,20)
        
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




        self.addMaxFileSize.setText("Максимальный размер файла:")
        self.addVC.setText("Видеовызов:")
        self.addOS.setText("Поддерживаемые ОС:")
        self.addVM.setText("Голосовые сообщения:")
        self.addGC.setText("Поддержка групповых чатов:")
        self.pushAdd = QPushButton("Добавить в базу")

        self.tab2.layout.addWidget(self.title)
        self.tab2.layout.addWidget(self.textbox)
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
        #Button func 
        self.pushAdd.clicked.connect(self.add_click)


        #THIRD TAB

        self.tab3.layout = QVBoxLayout(self)


        self.deletebox=QComboBox()

        self.deletebox.addItems(func.connectdb.array)



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
        self.title = QLabel("Выбор по функциональности:")
        self.filterFileSize = QComboBox()
        func.getCombolist(self.filterFileSize , func.connectdb.maxsize[0:-2])
        self.filterSupportVC = QComboBox()
        func.getCombolist(self.filterSupportVC , func.connectdb.oneOrZero[0:2])
        self.filterSupOS = QComboBox()
        func.getCombolist(self.filterSupOS , func.connectdb.operatingSyS[0:1])
        self.filterSupVM = QComboBox()
        func.getCombolist(self.filterSupVM , func.connectdb.oneOrZero[0:2])
        self.filterSupGC = QComboBox()
        func.getCombolist(self.filterSupGC , func.connectdb.oneOrZero[0:2])
        self.filterMaxFileSize = QLabel()
        self.filterVC = QLabel()
        self.filterOS = QLabel()
        self.filterVM = QLabel()
        self.filterGC = QLabel()
        



        self.filterMaxFileSize.setText("Максимальный размер файла:")
        self.filterVC.setText("Видеовызов:")
        self.filterOS.setText("Поддерживаемые ОС:")
        self.filterVM.setText("Голосовые сообщения:")
        self.filterGC.setText("Поддержка групповых чатов:")
        self.execDB = QPushButton("Фильтрация")



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

        self.execDB.clicked.connect(self.sort_click)





        
    @pyqtSlot()
    def sort_click(self):
        max_file_size = str(self.filterFileSize.currentIndex())
        op_system = str(self.filterSupOS.currentIndex())
        voice_messeges = str(self.filterSupVM.currentIndex())
        group_chat = str(self.filterSupGC.currentIndex())
        video_call = str(self.filterSupportVC.currentIndex())
        voice_messeges_str = "\n\t"
        group_chat_str = "\n\t"
        video_call_str = "\n\t"
        max_file_size_str = "\n\t"
        sort_arr = list()

        info_box.sort_func(voice_messeges,op_system,group_chat,video_call,max_file_size,sort_arr)

        voice_messeges_str = ", ".join(sort_arr[0])
        group_chat_str = ", ".join(sort_arr[1])
        video_call_str = ", ".join(sort_arr[2])
        max_file_size_str = ", ".join(sort_arr[3])

        sort_arr = list()
        



        sort_str = "Мессенджеры в которых:\n"+\
        func.connectdb.oneOrZero[int(voice_messeges)]+" поддержки голосовых сообщений в мессенджерах:\n\n"+voice_messeges_str+"\n\n"+\
        func.connectdb.oneOrZero[int(video_call)]+" поддержки видеовызова в мессенджерах:\n\n"+video_call_str+"\n\n"+\
        func.connectdb.oneOrZero[int(group_chat)]+" групповых чатов в мессенджерах:\n\n"+group_chat_str+"\n\n"+\
        "Мессенджеры которые поддерживают загрузку файлов размером "+func.connectdb.maxsize[int(max_file_size)]+":\n\n"+\
        max_file_size_str


        



        QMessageBox.information(self, "Уведомление", sort_str, QMessageBox.Ok)



    def delete_click(self):

        buttonreply = QMessageBox.question(self, 'Уведомление', "Вы действительно хотите удалить из базы?", QMessageBox.Yes | QMessageBox.Abort)
        if buttonreply == QMessageBox.Yes:
            self.dblist.clear()
            func.getCombolist(self.dblist, info_box.array)

            delete_title = self.deletebox.currentText()
            delete_id = self.deletebox.currentIndex()

            func.connectdb.del_db("all_messengers",delete_title)

            freeze(2)
            arr = []
            func.connectdb.array = info_box.ex_db(info_box.refresh_select,arr)
            self.dblist.clear()
            self.deletebox.clear()
            self.dblist.addItems(func.connectdb.array)
            self.deletebox.addItems(func.connectdb.array)


            QMessageBox.information(self, "Уведомление", str(delete_title) + "\nУдалён из базы данных" , QMessageBox.Ok)

        elif buttonreply == QMessageBox.Abort:
            QMessageBox.warning(self, "Cancel", "Действие отменено", QMessageBox.Abort)   
    def add_click(self):
        textboxValue = self.textbox.text()
        index_arr = (textboxValue, "0", self.addMaxSize.currentIndex(),\
            self.addSupportOS.currentIndex(),\
            self.addSupportVM.currentIndex(),\
            self.addSupportGC.currentIndex(),\
            self.addSupportVC.currentIndex())
        index_str = ""
        
       


        buttonreply = QMessageBox.question(self, 'Уведомление', "Вы действительно хотите добавить в базу?", QMessageBox.Yes | QMessageBox.Abort)
        if buttonreply == QMessageBox.Yes:
            info_box.insert_db(str(index_arr),index_arr[1])
            add_index=[self.addMaxSize.currentIndex(),self.addSupportOS.currentIndex()]
            io = self.addSupportOS.currentText()

            freeze(1)

            arr = []

            func.connectdb.array = info_box.ex_db(info_box.refresh_select,arr)

            self.dblist.clear()
            self.deletebox.clear()
            self.dblist.addItems(func.connectdb.array)
            self.deletebox.addItems(func.connectdb.array)


            QMessageBox.information(self, "Уведомление", textboxValue + "\nДобавлен" , QMessageBox.Ok)

        elif buttonreply == QMessageBox.Abort:
            QMessageBox.warning(self, "Cancel", "Действие отменено", QMessageBox.Abort)
    def import_click(self):


        import_index = self.dblist.currentIndex()
        import_name = self.dblist.currentText()
        bd_array =[]

        info_box.max_upload(import_name,bd_array)
        




        #ITS OK



        import_up =  func.connectdb.maxsize[bd_array[0][0]]
        import_gv = func.connectdb.oneOrZero[bd_array[0][1]]
        import_vm = func.connectdb.oneOrZero[bd_array[0][2]]
        import_vv = func.connectdb.oneOrZero[bd_array[0][3]]
        import_os = func.connectdb.operatingSyS[bd_array[0][4]]
        import_manufact = func.connectdb.manufact[bd_array[0][5]]







        

        
       
    
        buttonreply = QMessageBox.information(self, "Info about " + import_name,\
            "Название:\t\t\t" + import_name + \
            "\nМаксимальный размер файла: \t" + import_up + \
            "\nПоддержка групповых чатов:\t" + import_gv + \
            "\nПоддержка голосовых сообщений:\t" + import_vm + \
            "\nПоддержка Видеовызова:\t" + import_vv +\
            "\nПоддерживаемы ОС: \t\t" + import_os ,QMessageBox.Ok)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

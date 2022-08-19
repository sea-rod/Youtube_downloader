import sys
from download_thread import downlaod_thread
from search_thread import search_thread
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *




class window(QWidget):
      def __init__(self):
            super().__init__()
            self.t1=None
            self.flag = True
            self.setFixedSize(800,500)
            self.setWindowTitle("Youtube")
            self.setWindowIcon(QIcon("./images.png"))


      ########################## Font of the window ############################


            self.font = QFont()
            self.font.setPointSize(11)
            self.setFont(self.font)
            self.setStyleSheet("background-color:#7EC8E3;color:#050A30;")


      ######################### Progress Bar ############################


            self.bar = QProgressBar(self)
            self.bar.setStyleSheet('''
                                    QProgressBar
                                    {
                                    background-color:grey;
                                    border-radius:10px;
                                    text-align:center;
                                    font:bold;
                                    }
                                    QProgressBar::chunk
                                    {
                                    background-color:#0000FF;
                                    border-radius:10px;
                                    }''')
            self.bar.hide()


      ########################### Label "link" ####################


            self.label = QLabel(self)
            self.label.setText("Link:")
            self.label.move(70,150)
            self.label.setStyleSheet("font:bold;")


      ########################## line edit to enter the link ###############


            self.line_edit = QLineEdit(self)
            self.line_edit.move(110,149)
            self.line_edit.setFixedWidth(500)
            self.line_edit.setPlaceholderText("Enter Your Link Here")
            #self.line_edit.setStyleSheet("background-color:#000C66;")
            self.line_edit.setStyleSheet("Background-color:white;color:black")


      ################ Search button ###########################


            self.search_button = QPushButton(self)
            self.search_button.setText("Search")
            self.search_button.move(609,148)
            self.search_button.clicked.connect(self.yt_dwn)
            self.search_button.setStyleSheet("background-color:#0000FF;color:#000C66;font:bold;")


      ############################# res type mb combobox(dropdown menu) #######################


            txt = QLabel(self)
            txt.setText("Chose a option:")
            txt.move(120,200)
            txt.setStyleSheet("font:bold;")
            self.res = QComboBox(self)
            self.res.addItem("Resolution:360p Type:mkv Size:0Mb")
            self.res.move(120,220)
            self.res.setDisabled(True)
            self.res.setStyleSheet("background-color:white;color:grey")


      ############################### File Brower button ###########################


            txt2 = QLabel(self)
            txt2.setText("Select File Path:")
            txt2.move(400,200)
            txt2.setStyleSheet("font:bold;")
            path = QPushButton(self)
            path.move(599,219)
            path.setText("browser")
            path.setStyleSheet("background-color:#0000FF;color:#000C66;font:bold;")
            path.clicked.connect(self.brw_file)


      #################################################### Line edit to enter file path #################################


            self.path_label = QLineEdit(self)   
            self.path_label.move(400,220)
            self.path_label.setFixedWidth(200)
            self.path_label.setStyleSheet("background-color:white;color:black;")


      ################################ download button #################################


            self.button_dwn = QPushButton(self)
            self.button_dwn.setText("Download")
            self.button_dwn.move(350,300)
            self.button_dwn.clicked.connect(self.yt_dwnld_func)
            self.button_dwn.setCheckable(True)
            self.button_dwn.setDisabled(True)
            self.button_dwn.setStyleSheet("background-color:#0000FF;color:#000C66;font:bold")


################################## Function for the browser button ##########################


      def brw_file(self):
            self.fname = QFileDialog.getExistingDirectory(self,"","c:/users/DELL")
            self.path_label.setText(self.fname) 


######################################### Function for the search button, Finds the video stream ####################
      def yt_dwn(self):
            if self.t1 != None:
                  self.res.setStyleSheet("background:white;color:black;font-size:15px;")
                  self.res.removeItem(0)
                  self.res.addItems(self.t1.arr)
                  self.res.setEnabled(True)
                  self.button_dwn.setEnabled(True)
            else:
                  self.search_button.setDisabled(True)
                  link = self.line_edit.text()
                  print(link)
                  self.t1 = search_thread(link,self)
                  self.t1.finished.connect(self.yt_dwn)
                  self.t1.start()
      
      

######################################### Function for the download button, Downloads the video #######################


      def yt_dwnld_func(self,check):
            print(check)
            if check:
                  self.t2 = downlaod_thread(self.t1,self.fname,self.res.currentIndex())
                  self.button_dwn.setText("Cancel")
                  self.t2.start()
            else:
                  self.button_dwn.setText("Download")
                  self.t2.terminate()

##################################### Gets called each time a chuck of data has been downloaded ##########################


      def progress_fun(self,stream,chunk,bytes_r):
            self.flag = False
            self.bar.setGeometry(100,400,600,20)
            per = bytes_r/stream.filesize*100.0
            self.bar.setValue(int(100-per))
            self.bar.show()

##################################### Gets called the downloaded is complete ##########################

      def complete_dwnld(self,str_1,str_2):
            if self.flag:                                                     #str_1 print the object of yt
                  self.bar.setGeometry(100,400,600,20)                        #str_2 print the path of the file 
                  self.bar.setValue(100)
                  self.bar.show()
            self.search_button.setEnabled(True)
            self.button_dwn.setEnabled(True)

try:
      app = QApplication(sys.argv)
      app.setWindowIcon(QIcon("./images.png"))
      wid = window()
      wid.show()
except Exception:
      w = QWidget()
      txt = QLabel(w)
      txt.setGeometry(40,40,100,40)
      txt.setText("ERROR OCCURED !!!!!!!!!!!")
      w.show()
sys.exit(app.exec_())  #https://www.youtube.com/watch?v=h8ExvGymMaU

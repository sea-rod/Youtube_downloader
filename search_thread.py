from PyQt5.QtCore import QThread
from pytube import YouTube


class search_thread(QThread):
    
    dict_itags={}
    arr=[]

    def __init__(self,link,parent):
        super().__init__()
        self.link = link
        self.parent_1 = parent
    
    
    def run(self):
        self.yt = YouTube(self.link,on_progress_callback=self.parent_1.progress_fun,on_complete_callback=self.parent_1.complete_dwnld)
        self.streams=self.yt.streams.filter(progressive=True)
        for i,stream in enumerate(self.streams):
            self.dict_itags[i]=stream.itag
            self.arr.append(f"{i+1}.resolution:{stream.resolution} type:{stream.subtype} size:{self.cal_file_size(stream.filesize)}")
    
    
    def __del__(self):
        self.wait()


#################################### Calualtes the size of the Video ################################# 
    def cal_file_size(self,size):
      res = size/1024/1024
      if res >= 1000:
         return str(round(res/1024,2)) + "Gb"
      else:
         return str(round(res,2)) + "Mb"
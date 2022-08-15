from PyQt5.QtCore import QThread
from pytube import YouTube

class downlaod_thread(QThread):
    def __init__(self,t1,name,index) -> None:
        super().__init__()
        self.t1 = t1
        self.name = name
        self.index = index
    
    def run(self) -> None:
        stream = self.t1.yt.streams.get_by_itag(self.t1.dict_itags[self.index])
        stream.download(self.name)
        return super().run()
    
    def __del__():
        print("Thread stopped")
        pass


from threading import *
import time
import pyaudio
import wave
# 定义数据流块
CHUNK = 1024
class player(Thread):
    def init(self,filename):
        self.wf = wave.open(filename, 'rb')  # (sys.argv[1], 'rb')
        self.p = pyaudio.PyAudio()  # 创建一个播放器
    # def init(self,filename):
        # 打开数据流
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                             channels=self.wf.getnchannels(),
                             rate=self.wf.getframerate(),
                             output=True)
        # 读取数据
        self.data = self.wf.readframes(CHUNK)

        self.__flag =  Event()  # 用于暂停线程的标识
        self.__flag.set()
        self.ifdo = True
        self.isPlay = False
    def run (self):
        self.isPlay = True
        while self.ifdo and self.data != b'':
            self.__flag.wait()
            # time.sleep(2)

            # 播放
            self.stream.write(self.data)
            self.data = self.wf.readframes(CHUNK)
        # self.data = ''
        self.isPlay = False
        self.ifdo = False
        print("play finished")
    def pause(self):
        self.isPlay = False
        self.__flag.clear()  # 设置为False, 让线程阻塞
        print("pause")

    def resume(self):
        self.isPlay = True
        self.__flag.set()  # 设置为True, 让线程停止阻塞
        print("resume")
    def stop (self):
        print('I am stopping it...')
        self.isPlay=False
        self.ifdo = False



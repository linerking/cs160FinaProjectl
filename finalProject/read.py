import pickle
from database import *
import pymysql
from pynput.keyboard import Controller,Key,Listener
import wave
import pyaudio
(cur,con)= init()
#listen press
def search(path):
    cur.execute("select * from old where id = "+str(path))
    infor = cur.fetchall()
    try:
        print("22222")
        audio = infor[0][1]
        print("1111")
        play(audio)
    except:
        print("no audio was found")
def play(path):
    CHUNK = 1024
# 从目录中读取语音
    wf = wave.open(path, 'rb')
# read data
    data = wf.readframes(CHUNK)
# 创建播放器
    p = pyaudio.PyAudio()
# 获得语音文件的各个参数
    FORMAT = p.get_format_from_width(wf.getsampwidth())
    CHANNELS = wf.getnchannels()
    RATE = wf.getframerate()
    print('FORMAT: {} \nCHANNELS: {} \nRATE: {}'.format(FORMAT, CHANNELS, RATE))
# 打开音频流， output=True表示音频输出
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    frames_per_buffer=CHUNK,
                    output=True)
# play stream (3) 按照1024的块读取音频数据到音频流，并播放
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()

    p.terminate()
while True:
    # start_listen()
    a = input("input id")
    print(a)
    search(a)
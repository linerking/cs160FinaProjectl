import pickle
from database import *
import pymysql
from pynput.keyboard import Controller,Key,Listener
import wave
import pyaudio
import sys
import os
import termios
import time
import threading
from player import player
(cur,con)= init()
play = None
#listen press
def search1(path):
    global play
    play = player()    
    cur.execute("select * from old where id ="+str(path))
    infor = cur.fetchall()
    try:
        print("22222")
        audio = infor[0][1]
        print("1111")
        play.init(audio)
        play.start()
    except:
        print("no audio was found")

def plays(line,read):
    if (line == read and play != None):
        if play.isPlay and play.ifdo:
            play.pause()
        elif play.ifdo:
            play.resume()
        elif play.isPlay:
            play.stop()
            play.join()
        else:
            search1(line)
    else:
        if play != None:
            play.stop()
            play.join()
        search1(line)
    read = line

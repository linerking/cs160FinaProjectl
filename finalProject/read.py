import pickle
from database import *
import pymysql
from pynput.keyboard import Controller,Key,Listener
(cur,con)=init()
#listen press
id = ""
def on_press(key):
    global id
    try:
        id+=format(key.char)
    except:
        print("error")
    if len(id) == 10:
        cur.excute("select * from old where id = "+ id)
        try:
            audio = cur.fetchall()[0][1]
            play(audio)
        except:
            print("no audio was found")
        
#listen release
def on_release(key):
    print("已经释放:",format(key))
 
    if key==key.esc:
        # 停止监听
        return False
 
#start listing
def start_listen():
    print("hh")
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()



def play(audio):
    print(audio)

while True:
    start_listen()
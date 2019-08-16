import serial
from threading import *
import serial.tools.list_ports

class sensor(Thread):
    def init(self):
        self.play = False
        self.record = False
    def run (self):
        with serial.Serial('/dev/cu.usbmodem143101', 9600, timeout=100) as ser:
            while True:
                a = ser.readline()
                a = a.split(b',')[0]
                if (a == b'record'):
                    self.record = False
                elif(a == b'record\r\n'):
                    self.record = True
                elif (a == b'play'):
                    self.play = False
                elif(a==b'play\r\n'):
                    self.play = True

# port_list = list(serial.tools.list_ports.comports())
# for i in port_list:
#     print(i.device)
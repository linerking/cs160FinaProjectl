from threading import *
import sys



class keyboard(Thread):
    def init(self):
        self.input = ""
    def run (self):
        while True:
            print("emmm")
            read = False
            if  sys.stdin.isatty(): 
                print ("Have data!")
                for line in sys.stdin:
                    self.input = line
            else:
                print("no data")

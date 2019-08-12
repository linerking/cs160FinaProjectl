from recorder import *
import sys
from read import *
record = None
def search2(path):
    print("in search")
    global record
    record = recorder()
    value = "./audio/{}.wav".format(path)
    cur.execute("select * from old where id ="+str(path))
    infor = cur.fetchall()
    try:
        oldaudio = infor[0][1]
        updat = "update old set audio = '%s' where id = '%s'"
        cur.execute(updat%(value,path))
        record.init(value)
        record.start()
        con.commit()
    except:
        sql = "insert into old(id,audio) values( '{}', '{}' )".format(path,value)
        cur.execute(sql)
        record.init(value)
        record.start()
        con.commit()
def records(line,read):
    global record 
    if (line == read and record != None):
        if record.isPlay:
            record.stop()
            print("stop successed2")
            record.join()
            print("join successed")
            record = None
    else:
        print("searching2")
        try:
            print("inside try")
            if record.isPlay:
                record.stop()
                record.join()
                search2(line)
            print("out if")
        except:
            search2(line)

while True:
    print("emmm")
    read = False
    if  sys.stdin.isatty(): 
        print ("Have data!")
        reads = ""
        for line in sys.stdin:
            if (line == '1\n'):
                read = True
                print(read)
            elif (line == '0\n'):
                read = False
                print(read)
            elif read:
                plays(line,reads)
            else:
                records(line,reads)
            reads = line
    else:
        print("no data")
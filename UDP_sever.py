import socket
import re
import sqlite3
import csv
from pre_processdb import writetxt
from pre_processtxt import feature
from get_data import get_all_data
import numpy
from joblib import load
import os


BUFSIZE = 1000000
ip_port = ("", 1883)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ip_port)
text = []
OUTPATH = "/home/ubuntu/out"
model_path = '/home/ubuntu'
db_path = "/home/ubuntu/get"
csv_path = "/home/ubuntu/get"


def writecsv(csv_path):
    with open(csv_path + '/' + 'data.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n', )
        writer.writerow(['AvgX', 'AvgY', 'AvgZ', 'MedianX', 'MedianY', 'MedianZ', 'StdX',
                             'StdY', 'StdZ', 'MinX', 'MinY',
                             'MinZ', 'MaxX', 'MaxY', 'MaxZ', 'MeanMag',
                             'StdMag', 'MinMag', 'MaxMag', 'angle', 'aggravity_time'])
    print("finished build& written")


while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    text = data.decode(encoding='utf-8')
    text = text.strip('\n')
    print(text)
    if ';' in text:
        rec = re.findall(r"[-+]?[0-9]*\.?[0-9]+", text)
        print(rec)
        x = float(rec[0])
        y = float(rec[1])
        z = float(rec[2])
        params = [x,y,z]
        print(x)
        print(y)
        print(z)
        conn = sqlite3.connect(db_path+'/'+'test1.db')#database directory
        c = conn.cursor()
        print("Opened database successfully")
        c.execute("insert into accelerate (x,y,z) values (?, ?, ?)", params)
        conn.commit()
        print("Records created successfully")
        conn.close()
    elif text == 'p':
        writetxt(db_path, OUTPATH)
        writecsv(csv_path)
        final = feature(OUTPATH)
        data_len = len(final)
        for p in range(0, data_len):
            with open(csv_path + '/' + 'data.csv', 'a') as f:
                writer = csv.writer(f, delimiter=',', lineterminator='\n', )
                writer.writerow(final[p])
        all_data = get_all_data(csv_path)
        _all_data_x = []
        count = all_data.shape[0]
        for m in range(0, count):
            _all_data_x.append(all_data.iloc[m, 0:21])
        print(_all_data_x)
        clf_load = load(model_path+'/'+'falldefi-1.1.joblib')
        y_predict = clf_load.predict(_all_data_x)
        if y_predict[0] == 1:
            print('\033[1;31;40m')
            print('*' * 50)
            print('\033[5;31m fall down \033[1;31;40m')
            print('*' * 50)
            print('\033[0;37;40m')

        if y_predict[0] == 0:
            print('\033[1;32;40m')
            print('*' * 50)
            print('\033[5;32mall is well \033[1;32;40m')
            print('*' * 50)
            print('\033[0;37;40m')
    elif text == 'r':
        if os.path.exists(OUTPATH + '/' + 'test.txt'):
            os.remove(OUTPATH+'/'+'test.txt')
        if os.path.exists(csv_path + '/' + 'data.csv'):
            os.remove(csv_path + '/' + 'data.csv')
        conn = sqlite3.connect(db_path + '/' + 'test1.db')  # database directory
        c = conn.cursor()
        print("Opened database successfully")
        c.execute("DROP TABLE accelerate")
        conn.commit()
        print("Records cleaned successfully")
        c.execute('''create table accelerate(
                ID integer primary key AUTOINCREMENT,
                x real ,
                y real ,
                z real )''')  # create new table
        conn.close()
    else:
        print("input error")
    server.sendto(data.upper(), client_addr)
server.close()

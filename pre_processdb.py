import sqlite3
import os


def writetxt(a,b):
    db_dir = a
    if os.path.exists(b + '/' + 'test.txt'):
        os.remove(b + '/' + 'test.txt')
    f = open(b+'/'+'test.txt', 'a')
    conn = sqlite3.connect(db_dir+'/test1.db')
    c = conn.cursor()
    cursor = c.execute("SELECT *  from accelerate")
    for row in cursor:
        line = 'x = '+str(row[1])+','+'y = '+str(row[2])+',' + 'z = ' +str(row[3])+'\n'
        f.write(line)
        line = ''
    print("written in txt")
    conn.commit()
    conn.close()

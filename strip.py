file1 = open('/home/0-9.txt','a+')
file2 = open('/home/send.txt','a+')
for line in file1.readlines():
    print(line)
    line = line.replace('\n', ';\n')
    file2.write(line)
file1.close()
file2.close

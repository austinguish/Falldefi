import re
i = 0
a = "x=12.35,y=34.56,z= 65.21"
x_1 = re.findall(r"\d+\.?\d*", a)
for i in range(3):
    tmp = float(x_1[i])
    print(tmp)
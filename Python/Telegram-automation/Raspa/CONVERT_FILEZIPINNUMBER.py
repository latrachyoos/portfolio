import os
from time import sleep
my_list = os.listdir(r"C:\Users\latra\Desktop\filedata")
start = 1
for file in my_list:
    os.rename("C:\\Users\\latra\\Desktop\\filedata\\"+file, "C:\\Users\\latra\\Desktop\\filedata\\"+str(start) + file[len(file)-4:len(file)])

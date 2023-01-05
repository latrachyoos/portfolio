import os
import shutil
from time import sleep
my_list = os.listdir(r"C:\RASPAYOO\accdata")
start = 1
for file in my_list:
    if "acc" in file:
        try:
            file = open("C:\\RASPAYOO\\accdata\\"+file)
            dati = file.readline().split(";")
            file.close()
            print(dati[0])
            shutil.rmtree("C:\\Users\\latra\\Desktop\\tgdatabase\\" + str(dati[0]))
        except:
            pass

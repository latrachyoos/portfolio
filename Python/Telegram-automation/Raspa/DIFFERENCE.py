import os
import shutil

path1 = r"C:\Users\latra\Desktop\tgdatabase"
path2 = r"C:\Users\latra\Desktop\BACKUP DEI RASPA\backup doggo\accdata"
my_list = os.listdir(path1)
my_list2 = os.listdir(path2)

for file in my_list:
    if "," in file:
        file1 = file.replace(",","")
        os.rename(path1+"\\"""+file,path1+"\\"""+file1)

    pass
for file in my_list2:
    if "acc" in file:
        file = open(path2+"\\"+file, "r")
        dati = file.read().split(";")
        try:
            shutil.rmtree(path1+"\\"+dati[0])
            print(dati[0])
        except Exception as e :
            print(e)
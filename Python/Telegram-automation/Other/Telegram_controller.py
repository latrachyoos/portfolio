import os
from threading import Thread
def opens():
    os.system("start /wait cmd /c {python C:\PYTHONBOT\sban_remote.py}")
    #os.system("python C:\PYTHONBOT\sban_remote.py")
    print("aperto")
pc_name = ""
while True:
    comando = input("-comando: ")
    if "opennew" in comando:
        file = os.listdir("pc_controller")
        for k in range(100):

            if k < len(file):
                if not str(k) in file[k]:
                  file = open("pc_controller/"+str(k)+".txt","w")
                  file.write(str(k)+";"+comando.replace("new ",""))
                  file.close()
                  pc_name = k
                  break
            else:
                file = open("pc_controller/" + str(k) + ".txt", "w")
                file.write(str(k) + ";" + comando.replace("new ", ""))
                file.close()
                pc_name = k
                break
        file = open("sbanmulti_filetoread/" + str(pc_name) + ".txt", "w")
        file.write(str(pc_name) + ";" + comando.replace("opennew ", ""))
        file.close()
        print(pc_name)
        Thread(target=opens).start()


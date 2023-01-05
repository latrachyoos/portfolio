import os

my_list = os.listdir(r"G:\users\latra\desktop\tgdatabase")
vecchia = ""

for i in my_list:
    file = open("G:\\users\\latra\\desktop\\tgdatabase\\" + i + "\\notregistred.txt","w")
    file.close()
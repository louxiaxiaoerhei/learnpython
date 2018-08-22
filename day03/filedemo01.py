import os
import time
file_list = os.listdir("files")
# os.mkdir("files4")
print(file_list)

for temp in file_list:
    f = open("files/"+temp, "r", encoding="utf-8")

    str_temps = f.readlines()
    for str_temp in str_temps:
        f1 = open("files4/" + temp, "a", encoding="utf-8")
        if str_temp[0] != "#":
            time.sleep(2)
            f1.write(str_temp)
            f1.close()
    f.close()
    print("%s写完了" % temp)

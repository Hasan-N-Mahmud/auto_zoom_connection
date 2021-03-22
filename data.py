import datetime


list=[]
now = datetime.datetime.now()
day = now.strftime("%A")

f = open("Links.txt",'r')
flag = False
while(True):
    str = f.readline()
    if str.rstrip().lower() == day.lower():
        flag = True
    if flag:
        items = str.rstrip().split(",")
        if(len(items) > 1):
            list.append([items[0],items[1],items[2]])
    if str.rstrip() == 'EOD' and flag:
        break
print(list)
print("Data Loaded")
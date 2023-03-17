import csv
import pandas as pd
import numpy as np

# 返回里程大于5的占比
def percentage():
    file = pd.read_csv("../data/finaldata.csv")
    sum = 0
    five = 0
    for i in file['里程']:
        if i > 5:
            five += 1
        sum += 1
    return five/sum


# 返回近五年的年份
def year():
    list=[]
    with open("../data/finaldata.csv", encoding="utf-8", ) as file:
        f = csv.reader(file)
        for i in f:
            if i[2] != "生产":
                if i[2] not in list:
                    if int(i[2]) >= 2019:
                        list.append(i[2])
                else:
                    continue
    return np.unique(list)

# 返回近五年的年份对应的车辆
def car():
    list=[]
    year19=0
    year20=0
    year21=0
    year22=0
    year23=0
    with open("../data/finaldata.csv", encoding="utf-8", ) as file:
        f = csv.reader(file)
        for i in f:
            if i[2] != "生产":
                if i[2] == "2019":
                    year19+=1
                elif i[2] == "2020":
                    year20+=1
                elif i[2] == "2021":
                    year21+=1
                elif i[2] == "2022":
                    year22+=1
                elif i[2] == "2023":
                    year23+=1
        text=year19
        text1=year20
        text2=year21
        text3=year22
        text4=year23
        list.append(text)
        list.append(text1)
        list.append(text2)
        list.append(text3)
        list.append(text4)
    return list




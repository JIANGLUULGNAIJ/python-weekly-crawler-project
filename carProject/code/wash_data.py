import csv

with open("data/finaldata.csv", "w", encoding="utf-8", newline="")as file:
    f = csv.writer(file)
    with open("../data/newcardataover2.csv", "r", encoding="utf-8")as openfile:
        of = csv.reader(openfile)
        for i in of:
            if i[0] == "":
                f.writerow(['id', '品牌', '生产', '型号', '里程', '日期', '地区', '会员', '现价', '原价', '过户情况'])
            else:
                row = [i[0], (i[1])[:4].replace("系",""), (i[2])[:4], i[3], i[4].replace("万公里", ""), i[5], i[6], (i[7])[:2], i[8],
                       i[9].replace("万", ""), i[10]]
                f.writerow(row)

import csv
import requests
from bs4 import BeautifulSoup


with open("../data/car2.csv", "w", encoding="utf-8", newline="") as file:
    f=csv.writer(file)
    text = []
    list=["标题","里程","日期","地区","会员","原价","现价","过户情况"]
    f.writerow(list)

    for i in range(1, 42):
        url = "https://www.che168.com/zhejiang/baoma/a0_0msdgscncgpi1ltocsp%dexx0/?pvareaid=102179#currengpostion" % i
        resp = requests.get(url=url)
        soup = BeautifulSoup(resp.content, "html5lib")
        # print(soup)
        try:
            li = soup.find("ul", attrs={"class": "viewlist_ul"}).find_all("li")
        except Exception as e:
            print(e)

        # 获取数据
        for j in li:
            div = j.find("div", attrs={"class": "cards-bottom"})
            #  list=["标题","里程","日期","地区","会员","原价","现价","过户情况"]
            try:
                title = div.find("h4").text

                data = div.find("p").text.split("／")
                mileage = data[0]
                date = data[1]
                area = data[2]
                member = data[3]

                oprice = div.find("div", attrs={"class": "cards-price-box"}).find("s").text
                cprice = div.find("div", attrs={"class": "cards-price-box"}).find("em").text

                sum = 0
                for i in div.find("div", attrs={"class": "cards-price-box"}).find_all("i"):
                    sum += 1
                if sum == 0:
                    situation = "无"
                elif sum == 1:
                    situation = div.find("div", attrs={"class": "cards-price-box"}).find_all("i")[0].text
                else:
                    situation = div.find("div", attrs={"class": "cards-price-box"}).find_all("i")[0].text + "-" + \
                                div.find("div", attrs={"class": "cards-price-box"}).find_all("i")[1].text
            except Exception as e:
                print(e)
            car=[title,mileage,date,area,member,oprice,cprice,situation]
            print(car)
            text.append(car)
    f.writerows(text)



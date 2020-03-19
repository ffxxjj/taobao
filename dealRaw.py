from bs4 import BeautifulSoup
import re
import csv


def readTxt(i):
    with open("/Users/maxuan/Desktop/1/python/"+str(i)+".txt","r") as f:
        txt = f.read()
    return txt


def dealRawHtml(txt):
    soup = BeautifulSoup(txt,features="html.parser")
    return soup
  
  
def getBoxList(a):
    i = a.find("div",{"id":"mainsrp-itemlist"})
    small = i.find_all("div",{"data-category":"auctions"})
    return small


def getUseful(li):
    href = li.find("a",{"class":["pic-link","J_ClickStat","J_ItemPicA"]})["href"]
    print(href)
    money = li.find("strong").get_text()
    name = li.find("img")["alt"]
    list = []
    for t in li.find("span",class_="dsrs").next_siblings:
        list.append(t)
    shop = list[1]
    number = li.find("div",{"class":"deal-cnt"}).get_text()
    amount = number[:-3]
    place = li.find("div",{"class" : "location"}).get_text()
    return [name,amount,money,shop,href,place]
    
    
if __name__ == "__main__":
    txt = readTxt(1)
    a = dealRawHtml(txt)
    list = getBoxList(a)
    for li in list:
        getUseful(li)
'''
    with open("/Users/maxuan/Desktop/1/python/result/total.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(["产品名字","30天内收货人数","价格","店铺","url","收货地址"])
    for i in range(1,6):
        txt = readTxt(i)
        a = dealRawHtml(txt)
        list = getBoxList(a)
        for li in list:
            getUseful(li)
        with open("/Users/maxuan/Desktop/1/python/result/total.csv","a") as f:
            writer = csv.writer(f)
            for li in list:
                writer.writerow(getUseful(li))
    pass

'''

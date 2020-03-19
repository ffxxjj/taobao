from selenium import  webdriver
import time
urls= [
"https://s.taobao.com/search?q=%E5%8F%A3%E7%BA%A2&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=-11&ntoffset=-11&p4ppushleft=1%2C48&sort=sale-desc",
"https://s.taobao.com/search?q=%E5%8F%A3%E7%BA%A2&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=-11&p4ppushleft=%2C44&sort=sale-desc&s=44",
"https://s.taobao.com/search?q=%E5%8F%A3%E7%BA%A2&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=-11&p4ppushleft=%2C44&sort=sale-desc&s=88",
"https://s.taobao.com/search?q=%E5%8F%A3%E7%BA%A2&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=-11&p4ppushleft=%2C44&sort=sale-desc&s=132",
"https://s.taobao.com/search?q=%E5%8F%A3%E7%BA%A2&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=-11&p4ppushleft=%2C44&sort=sale-desc&s=176",
"https://s.taobao.com/search?q=%E5%8F%A3%E7%BA%A2&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=-11&p4ppushleft=%2C44&sort=sale-desc&s=220"]

i=1

for url in urls:
    driver = webdriver.Chrome(executable_path='/Users/maxuan/Desktop/课程/1/chromedriver')
    driver.get(url)
    time.sleep(60)
    print(driver.page_source)
    with open("/Users/maxuan/Desktop/1/python/"+str(i)+".txt","w") as f:
        f.write(driver.page_source)
    i = i+1
    driver.close()




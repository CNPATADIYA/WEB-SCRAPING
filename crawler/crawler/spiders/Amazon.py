import requests
import scrapy
from bs4 import BeautifulSoup
from ..items import CrawlerItem
import os

class AmazonSpider(scrapy.Spider):
    name = 'amazonspider'
    start_urls = ['https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=on&p%5B%5D=facets.brand%255B%255D%3DRealme&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DApple&sort=popularity',
                  'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=on&p%5B%5D=facets.brand%255B%255D%3DRealme&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DApple&sort=popularity&page=2',
                  'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=on&p%5B%5D=facets.brand%255B%255D%3DRealme&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DApple&sort=popularity&page=3',
                  'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=on&p%5B%5D=facets.brand%255B%255D%3DRealme&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DApple&sort=popularity&page=4',
                  'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=on&p%5B%5D=facets.brand%255B%255D%3DRealme&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DApple&sort=popularity&page=5'
                  ]

    def parse(self,response):
        items = CrawlerItem()
        page = requests.get(AmazonSpider.start_urls[0])
        sp = BeautifulSoup(page.content, 'html.parser')
        product = sp.findAll('div', {'class': '_3wU53n'})
        sp = response.css('div._3e7xtJ')
        rating = sp.css('div.hGSR34::text').extract()
        price = sp.css('._2rQ-NK::text').extract()
        temp = sp.css('._38sUEc span span:nth-child(1)::text').extract()
        No_of_people_give_rating = []
        for x in temp:
            No_of_people_give_rating.append(x.split(' ')[0])
        for i in range(0,len(price)):
            items['product'] = product[i].text
            items['price'] = price[i]
            items['rating'] = rating[i]
            items['No_of_people_give_rating'] = No_of_people_give_rating[i].strip()
            yield items


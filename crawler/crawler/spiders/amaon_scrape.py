"""The advent of internet and smartphones has been an impetus to the e-commerce industry. With millions of customers and billions of dollars at stake, the market has started seeing the multitude of players. Which in turn has led to rise of e-commerce aggregator platforms which collect and show you the information regarding your products from across multiple portals? For example when planning to buy a smartphone and you would want to see the prices at different platforms at a single place. What does it take to build such an aggregator platform? Here’s my small take on building an e-commerce site scraper."""
"""
import scrapy
def isnumeric(x):
    if(type(x)!=int):
        return False
    else:
        return True
class amaon_scrape(scrapy.Spider):
    name='amazon'
    start_urls=['https://www.amazon.in/b?node=16382860031&pf_rd_r=KEA9VSE22MH335031JZB&pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e']
    def parse(self, response):
        product_name=response.css('.a-text-normal::attr(data-attribute)').extract()
        c=response.css('.a-color-secondary::text').extract()#2,8,14,20,are useful
        company_name=[]
        for i in c:
            if (i==' and ' or i=='by ' or i=='You Save: ' or i=='See available choices' or i=='More Buying Choices' or i=='(3 offers)' or i=='FREE Delivery ' or i=='(5 offers)' or i=='(4 offers)'or i=='(2 offers)'):
                continue
            else:
                company_name.
        image=response.css('.cfMarker::attr(src)').extract()
        price=response.css('.s-price::text').extract()
        rating=response.css('.a-icon-alt::text').extract()
        n_o_p=[]
        x=response.css('.a-link-normal::text').extract()
        for iems in x:
            if (iems=='See Details' or iems==' with coupon' or iems=='new'):
                continue
            else:
                n_o_p.append(iems)


        for z in zip(product_name,price,n_o_p,rating,image):
            scrapped_info={
                "product_name:":z[0],
                "Price:":z[1],
                "NO of People likes:":z[2],
                "Ratings:":z[3],
                "Image":z[4],
            }
        yield {'comapny name=:' : company_name}
        #https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/"""
import scrapy

class ShopcluesSpider(scrapy.Spider):
   #name of spider
   name = 'shopclues'

   #list of allowed domains
   allowed_domains = ['www.shopclues.com/mobiles-featured-store-4g-smartphone.html']
   #starting url
   start_urls = ['http://www.shopclues.com/mobiles-featured-store-4g-smartphone.html/']
   #location of csv fil


   def parse(self, response):
       #Extract product information
       titles = response.css('img::attr(title)').extract()
       images = response.css('img::attr(data-img)').extract()
       prices = response.css('.p_price::text').extract()
       discounts = response.css('.prd_discount::text').extract()


       for item in zip(titles,prices,images,discounts):
           scraped_info = {
               'title' : item[0],
               'price' : item[1],
               'image_urls' : item[2], #Set's the url for scrapy to download images
               'discount' : item[3]
           }

           yield scraped_info
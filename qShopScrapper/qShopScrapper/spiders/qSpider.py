import scrapy

from qShopScrapper.items import qSwitchGameItem
import qShopScrapper.constant as c 


class QspiderSpider(scrapy.Spider):
    name = "qSpider"
    allowed_domains = ["www.qisahn.com"]
    start_urls = ["https://www.qisahn.com/pg/nintendo-nintendo-switch-games-brand-new"]

    #get the item info 
    def parse(self, response):
        
        #get all card product
        products = response.css('div.product-wrapper')

        for p in products:
            
            gameItem = qSwitchGameItem()
            
            # title retrived at this page maybe incomplete.
            # update at from detail page
            gameItem['title']= p.css('div.product-name-wrapper a::text').get()

            itemUrl:str = c.BASE_PAGE_URL+p.css('div.product-name-wrapper a::attr(href)').get()
            gameItem['url']=itemUrl

            gameItem['price']= None if not p.css('div.product-price::text').get().strip() else p.css('div.product-price::text').get().strip()
            gameItem['description']=None

            if itemUrl:

                request = scrapy.Request(itemUrl,callback=self.parseDetailPage)   
                request.meta['item'] = gameItem

                yield request

            else:
                yield gameItem


        #go to the page and continue parsing
                
        #select the next button
        nxtPage = response.xpath("//li[@class='next_page']/a[@rel='next']/@href").get()

        #go to next page for parsing, if there is next btn =>  exist next page link
        if nxtPage:
            full_nxtPage_url:str = c.BASE_PAGE_URL + nxtPage
            yield response.follow(full_nxtPage_url, callback=self.parse)




        
    #go to the detail page and extract description and title ????
    def parseDetailPage(self,response):
        
        currItem = response.meta['item']
        
        desc:list = response.xpath("//div[@class='product_text']//text()").getall()

        title:str = response.xpath("//h1[@id='product_base_name']/text()").get().strip()

        currItem['description'] =desc
        
        #update the title since the the title from start page can be incompelete
        if currItem['title'] != title:
            currItem['title'] = title            

        yield currItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from dotenv import  dotenv_values,load_dotenv,find_dotenv
import os
import mysql.connector

config = dotenv_values(find_dotenv())

class QshopscrapperPipeline:
    def process_item(self, item, spider):
        return item

class qProductProcessPipeline:

    def process_item(self, item, spider):
  
        adapter = ItemAdapter(item)


        #for price,remove the dollar sign and convert to float
        _price:str = adapter.get('price')
        
        if _price:
            adapter['price'] = self.priceProcess(_price)



        if adapter.get('description'):

            lis:list = adapter.get('description')

            #convert to stringText
            adapter['description'] = self.textListToString(lis)


        return item

    def textListToString(self,lis:list):
        
        # finalDesc:str = ''.join([x.strip() for x in lis if  x !='\n'])

        finalDesc:str = ''
        for x in lis:
            if x != '\n':
                finalDesc += x.strip()

        return finalDesc
    
    def priceProcess(self,s1:str)->float:
        
        #handle when there is price range like "$59.90 - $68.90"
        #choose the the lowest price 

        _temp:str = s1.split('-')[0]

        #remove dollar sign and whitespace
        _temp = _temp.replace("$","").strip()

        return float(_temp)

class SaveToMySQLPipeline:

    def __init__(self):

        #create .env file within same folder as the pipeline file 

        #alternative way to load values from .env file
        # load_dotenv()
        # test = os.environ['PASSWORD']
        # print(test)

        self.conn = mysql.connector.connect(

            host =  config['HOST'],
            user =  config['USER'],
            password = config['PASSWORD'],
            database = config['DB_NAME']

        )

        ## Create cursor, used to execute commands
        self.cur = self.conn.cursor()

        # Create switchGames table if none exists
        # make title col unqiue to prevent re-inserting 
        # price col need to be decimal and having 2 decimal place 

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS switchGames(
            id int NOT NULL auto_increment, 
            title VARCHAR(255) NOT NULL,
            url VARCHAR(255),
            price DECIMAL(10,2),
            description text,
            PRIMARY KEY (id),
            unique (title)
                         
        )
        """)

    def process_item(self, item, spider):

        ## perfrom  upsert 
        #likely to update price and url only 
        #insert if this a new record 
        self.cur.execute(""" insert into switchGames (
            title, 
            url, 
            price,
            description
            ) values (
                %s,
                %s,
                %s,
                %s
                )
            as new
            ON DUPLICATE KEY UPDATE
            url = new.url,
            price = new.price;                                                    
            """, (
            item["title"],
            item["url"],
            item["price"],
            item["description"]
        ))

        # ## Execute insert of data into database
        self.conn.commit()
        return item

    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.conn.close()
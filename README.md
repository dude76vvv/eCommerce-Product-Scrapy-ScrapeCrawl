# eCommerce-Product-Scrapy-ScrapeCrawl 
The aim of this project is to use Python Scrapy library to crawl and scrape product information from website.<br/>
Brand new Nintendo Switch game product-details will be scraped from popular video game store **[Qisahn](https://www.qisahn.com/)** eCommerce site for demonstration. 

Information such as product title, description and price is captured and store in database. 

## Features
* Multi-page web-crawl and scraping of product information
* Scraped data archived into MySQL database 
  
## Technologies used
* Scrapy 
* MySQL

## Setting up

1. **CD** to the project folder and create virtual environment.
    - **python -m venv .venv**

2. Activate virtual environment
    - **.venv\Scripts\activate**

3. Install the required modules needed for application to run:
    - **pip install -r requirements.txt**
  
4. Edit the .env with own database credentials to allow connection

![image](https://github.com/dude76vvv/eCommerce-Product-Scrapy-ScrapeCrawl/assets/131178280/f88587eb-9c25-4151-abc2-1ff00c6256cb)



## Running
1. **CD** to the qShopScrapper folder and list the spider available.
    - **scrapy list**
      
![image](https://github.com/dude76vvv/eCommerce-Product-Scrapy-ScrapeCrawl/assets/131178280/7c8c38ca-c826-4a68-a823-f4896c9595ac)
 
2. Run the below command to the start webcrawl & scrape with the spider "**qSpider**". (_this will also perform upsert to the database_).
    - **scrapy crawl qSpider**


![image](https://github.com/dude76vvv/eCommerce-Product-Scrapy-ScrapeCrawl/assets/131178280/de86b4e0-71a6-4215-af5e-973d28721944)

  
3. Run the below command to the start webcrawl & scrape with the spider "**qSpider**" **+** generate .json file. (_this will also perform upsert to the database_).
    - **scrapy crawl qSpider -O scraped.json**


  
## Screenshots

![image](https://github.com/dude76vvv/eCommerce-Product-Scrapy-ScrapeCrawl/assets/131178280/bd0165b5-6f78-4ac2-ae21-57cc652d5fdb)

![image](https://github.com/dude76vvv/eCommerce-Product-Scrapy-ScrapeCrawl/assets/131178280/551f7a74-de8a-4bce-8686-82e961de7703)

![image](https://github.com/dude76vvv/eCommerce-Product-Scrapy-ScrapeCrawl/assets/131178280/105265b1-7ebb-4cce-a15c-0cb1c09048a6)





import json
import scrapy 
from scraper.scraper.items import com_details_item

class scraper_spider(scrapy.Spider):
    name = "collect_cart_data"
    start_urls = [
        'https://www.startech.com.bd/adata-4gb-ddr3-1600-bus'
    ]

      # this is what start_urls does
      # def start_requests(self):
      #     urls = ['https://www.theodo.co.uk/team',]
      #     for url in urls:
      #       yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pname = response.css("h1.product-name::text")[0].extract()
        pprice = response.css("td.product-price::text")[0].extract()
        img = response.css("a.thumbnail img::attr(src)")[0].extract()
        details = {
            'prod_name' : pname,
            'price' : pprice,
            'img' : img
        }
        j_format = json.dumps(details)
        print(j_format)
        yield j_format


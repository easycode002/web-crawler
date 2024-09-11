from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlSpider(CrawlSpider):
    # for class name to use in run
    name="crawler"
    allow_domains = ["books.toscrape.com"] # https://books.toscrape.com/
    start_urls = ["https://books.toscrape.com/"]

    rules = (
        # Extract links for categories
        Rule(LinkExtractor(allow="catalogue/category")),
        # Extract book detail links and call parse_item
        Rule(LinkExtractor(allow="catalogue",deny="catalogue"), callback="parse_item")
    )

    # Define a function for handle scrap with specific on element tag
    def parse_item(self,response):
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "availability": response.css(".availability::text")[-1].getall().strip() #.replace("\n", "").replace(" ","")
        }
import scrapy


class DataanalystspiderSpider(scrapy.Spider):
    name = "dataanalystspider"
    allowed_domains = ["www.reed.co.uk"]
    start_urls = ["https://www.reed.co.uk/jobs/data-analyst-jobs"]

    def parse(self, response):
        pass

import scrapy


class daoshiSpider(scrapy.Spider):
    name = "daoshi"
    start_urls = ["http://yz.kaoyan.com/scnu/daoshi/22/508530/"]
    
    def parse(self, response):
        for url in response.xpath('//div[@class="articleCon"]/table/tbody/tr/td/a/@href'):
             full_url = response.urljoin(url.extract())
             yield scrapy.Request(full_url,callback=self.parse_content)
             
             
    def parse_content(self,response):
        print(response.xpath('//div[@class="waper"]/div/div/div/h1/text()').extract()[0])
        print(response.xpath('//div[@class="waper"]/div/div/div/div[@class="articleCon"]/p/text()').extract())
        yield{
            "name":response.xpath('//div[@class="waper"]/div/div/div/h1/text()').extract()[0],
            "jieshao":response.xpath('//div[@class="waper"]/div/div/div/div[@class="articleCon"]/p/text()').extract()
        }
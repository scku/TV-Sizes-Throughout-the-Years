from scrapy.spider import Spider
from scrapy import Selector
from cnettv.items import CnettvItem
from scrapy.http import Request

XPATH_PRODUCT = '//section[@class="searchItem product"]/a/@href'
XPATH_NEXT = '//*[@id="dfllHeading"]/div/div[2]/a[@class="next"]/@href'

class MySpider(Spider):
	name = "cnettv"
	allowed_domains = ["www.cnet.com"]
	start_urls = ["http://www.cnet.com/topics/tvs/products/"]

	def parse(self, response):
		hxs = Selector(response)

		next_page = hxs.xpath(XPATH_NEXT).extract()
		#print "Next page url:{0}".format(next_page)
		for link in next_page:
			tmp = "http://www.cnet.com" + link
			yield Request(tmp, self.parse)

		product_links = hxs.xpath(XPATH_PRODUCT).extract()
		for link in product_links:
			item = CnettvItem()
			item["link"] = "http://www.cnet.com" + link
			yield item


import scrapy

class firstSpider(scrapy.Spider):
	"""A first sample spider"""
	name = "Sample"
	allowed_domains = ["incredibleindia.org"]
	start_urls = ["http://incredibleindia.org/index.php/travel/destination"]
	def parse(self, response):
		destinationsList = []
		for sel in response.xpath('//ul/li'):
			link = sel.xpath('a/@href').extract()
			linkslist = link[0].split('/')
			if len(linkslist) < 5:
				continue
			elif linkslist[len(linkslist) - 2] <> 'destination':
				continue
			else:
				destinationsList.append(linkslist[len(linkslist) - 1])
		pass

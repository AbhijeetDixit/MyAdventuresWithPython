import scrapy

class firstSpider(scrapy.Spider):
	"""A first sample spider"""
	name = "Sample"
	allowed_domains = ["incredibleindia.org"]
	start_urls = ["http://incredibleindia.org/index.php/travel/destination"]
	def parse(self, response):
		destinationsList = []
		base_url = "http://incredibleindia.org"
		for sel in response.xpath('//ul/li'):
			link = sel.xpath('a/@href').extract()
			linkslist = link[0].split('/')
			if len(linkslist) < 5:
				continue
			elif linkslist[len(linkslist) - 2] <> 'destination':
			 	continue
			else:
				destinationsList.append(linkslist[len(linkslist) - 1])
				new_url = base_url+link[0]
				with open("data/01list.txt","a") as f:
					f.write(linkslist[len(linkslist) - 1] + "\n")
				request = scrapy.Request(new_url, callback=self.parse_destination_page)
				request.meta['place'] = linkslist[len(linkslist) - 1]
				yield request
		pass

	def parse_destination_page(self, response):
		base_url = "http://incredibleindia.org"
		for sel in response.xpath('//ul/li'):
			link = sel.xpath('a/@href').extract()
			linkslist = link[0].split('/')
			if len(linkslist) < 6:
				continue
			else:
				sublist = linkslist[len(linkslist) - 1].split('-')
				if sublist[len(sublist) - 1] <> 'introduction':
					continue
				else:
					new_url = base_url+link[0]
					request = scrapy.Request(new_url, callback=self.parse_destination_intro)
					request.meta['place'] = response.meta['place']
					yield request
			pass
		pass

	def parse_destination_intro(self, response):
		filename = 'data/' + response.meta['place'] + '.txt'
		for sel in response.xpath('//div[@class="article-full-div"]/div[@class="main-madurai"]/div[@class="madurai-right"]/div[@class="madurai-right-one"]'):
			desc = sel.xpath('text()').extract()
			if type(desc[0]) <> 'list':
				with open(filename,"a") as f:
					f.write(desc[0] + '\n')
			else:
				for string in desc[0]:
					with open(filename,"a") as f:
						f.write(string + ' ')
					pass
				with open(filename, "a") as f:
					f.write('\n')
			pass
			sub_desc = sel.xpath('div/text()').extract()
			if sub_desc:
				if type(sub_desc[0]) <> 'list':
					with open(filename, "a") as f:
						f.write(sub_desc[0] + '\n')
				else:
					for string in desc[0]:
						with open(filename, "a") as f:
							f.write(string + ' ')
						pass
					with open(filename, "a") as f:
						f.write('\n')
				pass
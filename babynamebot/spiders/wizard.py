import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from babynamebot.items import NameList


class WizardSpider(Spider):
	name = "Wizard"
	start_urls = [
		"http://www.babynamewizard.com/international-names-lists-popular-names-from-around-the-world"
	]

	def parse(self, response):
		""" This function parses a sample response. Some contracts are mingled
		with this docstring.

		@url http://www.babynamewizard.com/international-names-lists-popular-names-from-around-the-world
		@returns requests 1
		"""
		
		item_urls = response.xpath("//a[text()='Boys' or text()='Girls']/@href").extract()
		
		for item_url in item_urls:
			yield scrapy.Request(item_url, self.parse_item)
		
	def parse_item(self, response):
		""" This function parses a sample response. Some contracts are mingled
		with this docstring.

		@url http://www.babynamewizard.com/name-list/english-girls-names-most-popular-names-for-girls-in-england
		@returns items 1 1
		@scrapes gender country region names
		"""
		
		title = response.xpath(".//*[@id='page-title']/text()")
		gender = title.re_first(r'(Boy|Girl)')

		item = NameList()
		item['gender'] = 'male' if gender == 'Boy' else 'female'
		item['country'] = title.re_first(r'in ([A-Z a-z]+)(?: \([A-Z a-z]+\))?').strip()
		item['region'] = title.re_first(r'in [A-Z a-z]+(?:\(([A-Z a-z]+)\))?').strip()
		
		item['names'] = response.xpath(".//*[@class='item-list']/ol/li//text()").extract()
		
		return item
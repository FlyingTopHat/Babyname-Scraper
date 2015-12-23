from scrapy.exceptions import DropItem


class UpperCaseNamesPipeline(object):
	"""A pipeline for converting names to uppercase"""

	def process_item(self, item, spider):
	
		item['names'] = [name.upper() for name in item['names']]
		return item
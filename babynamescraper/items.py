from scrapy.item import Item, Field

class NameList(Item):

	country = Field()
	region = Field()
	names = Field()
	gender = Field()
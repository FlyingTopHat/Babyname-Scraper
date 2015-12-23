# Scrapy settings for babynamebot project

SPIDER_MODULES = ['babynamebot.spiders']
NEWSPIDER_MODULE = 'babynamebot.spiders'
DEFAULT_ITEM_CLASS = 'babynamebot.items.Website'

ITEM_PIPELINES = {
	'babynamebot.pipelines.UpperCaseNamesPipeline':1,	
}
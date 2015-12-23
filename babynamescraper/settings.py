# Scrapy settings for babynamescraper project

SPIDER_MODULES = ['babynamescraper.spiders']
NEWSPIDER_MODULE = 'babynamescraper.spiders'
DEFAULT_ITEM_CLASS = 'babynamescraper.items.NameList'

ITEM_PIPELINES = {
	'babynamescraper.pipelines.UpperCaseNamesPipeline':1,	
}
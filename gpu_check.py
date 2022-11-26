from decimal import Decimal

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from gpu_item import GpuItem


class GPUCheck(CrawlSpider):
    name = 'gpu_check'
    allowed_domains = ['gpucheck.com']
    start_urls = ['https://www.gpucheck.com/graphics-cards']
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
        'ITEM_PIPELINES': {
            'pipelines.DynamoDbPipeline': 300, #numero de ejecución
        }
    }

    rules = (
        Rule(LinkExtractor(allow=('/gpu/', )), callback='parse_item'),
    )


    def parse_item(self, response):
        self.logger.info('A response from %s just arrived!', response.url)

        item = GpuItem()
        summary_table = response.xpath('//div[@id="summary"]/table/tbody/tr')

        for row in summary_table:
            key = row.xpath('th/text()').get().strip().lower().replace(' ', '_')

            if not key:
                item.name = row.xpath('td/text()').get().strip()

            elif key == 'price':
                item.currency, item.price = row.xpath('td/text()').get().strip().split()
                item.price = Decimal(item.price.replace(',', ''))

            elif key in item.__dataclass_fields__:
                setattr(item, key, row.xpath('td/text()').get().strip())

        return item
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime

class ImdbscraperPipeline:
    def process_item(self, item, spider):
        return item

class SecondsToReal:

    def process_item(self, item, spider):

        adaptor = ItemAdapter(item)

        adaptor['movie_length'] = str(datetime.timedelta(seconds=adaptor['movie_length'][0]))

        return item   
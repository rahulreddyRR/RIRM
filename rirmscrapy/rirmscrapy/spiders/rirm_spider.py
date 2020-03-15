from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
# from scrapy.item import Item, Field
#
# class MyItem(Item):
#     url= Field()
#
#
# class someSpider(CrawlSpider):
#     name = 'crawltest'
#     allowed_domains = ['quotes.toscrape.com']
#     start_urls = ['http://quotes.toscrape.com/']
#     rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)
#
#     def parse_obj(self,response):
#         item = MyItem()
#         item['url'] = []
#         for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
#             item['url'].append(link.url)
#
#         for i in range(len(item)):
#             for j in item.values():
#                 print(i," : ", j)
#         return item
#

# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors import LxmlLinkExtractor
from rirmscrapy.items import MyItem
import csv

class someSpider(CrawlSpider):
  name = 'test'
  allowed_domains = ['quotes.toscrape.com']
  start_urls = ['http://quotes.toscrape.com/']

  rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)


  def parse_obj(self,response):
    item = MyItem()
    for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
        item['url'].append(link.url)
        # with open('protagonist.csv', 'w', newline='') as file:
        #   writer = csv.writer(file)
        #   writer.writerows(item[0])
        yield item

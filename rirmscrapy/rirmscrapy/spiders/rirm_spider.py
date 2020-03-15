from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from rirmscrapy.items import MyItem

class someSpider(CrawlSpider):
  name = 'test'
  allowed_domains = ['quotes.toscrape.com']
  start_urls = ['http://quotes.toscrape.com/']

  rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)


  def parse_obj(self,response):
    item = MyItem()
    for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
        item['url'].append(link.url)
        yield item

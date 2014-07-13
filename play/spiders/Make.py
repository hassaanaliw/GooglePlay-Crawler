from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from play.items import PlayItem
from scrapy.http import Request



class books_and_reference(BaseSpider):
     name = 'books_and_reference'  
     allowed_domains = ["play.google.com"]

     with open('links/BOOKS_AND_REFERENCE.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class business(BaseSpider):
     name = 'business'  
     allowed_domains = ["play.google.com"]

     with open('links/BUSINESS.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class comics(BaseSpider):
     name = 'comics'  
     allowed_domains = ["play.google.com"]

     with open('links/COMICS.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class communication(BaseSpider):
     name = 'communication'  
     allowed_domains = ["play.google.com"]

     with open('links/COMMUNICATION.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class education(BaseSpider):
     name = 'education'  
     allowed_domains = ["play.google.com"]

     with open('links/EDUCATION.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class entertainment(BaseSpider):
     name = 'entertainment'  
     allowed_domains = ["play.google.com"]

     with open('links/ENTERTAINMENT.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class finance(BaseSpider):
     name = 'finance'  
     allowed_domains = ["play.google.com"]

     with open('links/FINANCE.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class health_and_fitness(BaseSpider):
     name = 'health_and_fitness'  
     allowed_domains = ["play.google.com"]

     with open('links/HEALTH_AND_FITNESS.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class libraries_and_demo(BaseSpider):
     name = 'libraries_and_demo'  
     allowed_domains = ["play.google.com"]

     with open('links/LIBRARIES_AND_DEMO.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class lifestyle(BaseSpider):
     name = 'lifestyle'  
     allowed_domains = ["play.google.com"]

     with open('links/LIFESTYLE.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class media_and_video(BaseSpider):
     name = 'media_and_video'  
     allowed_domains = ["play.google.com"]

     with open('links/MEDIA_AND_VIDEO.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class medical(BaseSpider):
     name = 'medical'  
     allowed_domains = ["play.google.com"]

     with open('links/MEDICAL.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class music_and_audio(BaseSpider):
     name = 'music_and_audio'  
     allowed_domains = ["play.google.com"]

     with open('links/MUSIC_AND_AUDIO.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class news_and_magazines(BaseSpider):
     name = 'news_and_magazines'  
     allowed_domains = ["play.google.com"]

     with open('links/NEWS_AND_MAGAZINES.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class personalization(BaseSpider):
     name = 'personalization'  
     allowed_domains = ["play.google.com"]

     with open('links/PERSONALIZATION.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class photography(BaseSpider):
     name = 'photography'  
     allowed_domains = ["play.google.com"]

     with open('links/PHOTOGRAPHY.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class productivity(BaseSpider):
     name = 'productivity'  
     allowed_domains = ["play.google.com"]

     with open('links/PRODUCTIVITY.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class shopping(BaseSpider):
     name = 'shopping'  
     allowed_domains = ["play.google.com"]

     with open('links/SHOPPING.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class social(BaseSpider):
     name = 'social'  
     allowed_domains = ["play.google.com"]

     with open('links/SOCIAL.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class sports(BaseSpider):
     name = 'sports'  
     allowed_domains = ["play.google.com"]

     with open('links/SPORTS.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class tools(BaseSpider):
     name = 'tools'  
     allowed_domains = ["play.google.com"]

     with open('links/TOOLS.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class transportation(BaseSpider):
     name = 'transportation'  
     allowed_domains = ["play.google.com"]

     with open('links/TRANSPORTATION.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class travel_and_local(BaseSpider):
     name = 'travel_and_local'  
     allowed_domains = ["play.google.com"]

     with open('links/TRAVEL_AND_LOCAL.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class weather(BaseSpider):
     name = 'weather'  
     allowed_domains = ["play.google.com"]

     with open('links/WEATHER.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item


class widgets(BaseSpider):
     name = 'widgets'  
     allowed_domains = ["play.google.com"]

     with open('links/WIDGETS.txt','r') as fil:
           start_urls = [i.strip() for i in fil.readlines()]

     def parse(self,response):
             hxs     = HtmlXPathSelector(response)
             titles = hxs.select('//h2/a[@class = "title"]')
             for title in titles :
                      item = PlayItem()
                      item["title"] = title.select("text()").extract()
                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
                      yield item



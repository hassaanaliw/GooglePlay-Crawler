__author__ = 'Hassaan'
def main():
    file = open("Make.py",'wb')
    file.write("from scrapy.spider import BaseSpider\n"
                     "from scrapy.selector import HtmlXPathSelector\n"
                     "from play.items import PlayItem\n"
                     "from scrapy.http import Request\n"
                     "\n"
                     "\n"
                     "\n")
    new = open("W.txt","r")

    three = '''             titles = hxs.select('//h2/a[@class = "title"]')\n'''



    lines = new.readlines()
    for i in lines:
      thisline = i.split(" ")
      for a in thisline:

          file.write(




                     "class %s(BaseSpider):\n"
                     "     name = '%s'  \n"
                     '     allowed_domains = ["play.google.com"]\n'
                     "\n"
                     "     with open('links/%s.txt','r') as fil:\n"
                     "           start_urls = [i.strip() for i in fil.readlines()]\n"
                     "\n"
                     "     def parse(self,response):\n"
                     "             hxs     = HtmlXPathSelector(response)\n" %(a.lower(),a.lower(),a) )

          file.write(three)







          file.write( "             for title in titles :\n"
                     "                      item = PlayItem()\n"
                     '                      item["title"] = title.select("text()").extract()\n'
                     '''                      item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]\n'''
                     "                      yield item\n"
                     "\n"
                     "\n")










main()
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import sys
from scr_l_mysql.items import SMItem

class DmozSpider(BaseSpider):
    name = "scrdav"
    allowed_domains = ["-----"]
    start_urls = [
        "------"
    ]

    def parse(self, response):
           hxs = HtmlXPathSelector(response)
           items = []
           item = SMItem()
           row1=hxs.select('//title/text()').re(r'DPCC ::\s*(.*)data')
           row2= hxs.select('//tr[2]/td[2]/text()').extract()
           row3= hxs.select('//tr[2]/td[3]/text()').extract()
           row4= hxs.select('//tr[2]/td[4]/text()').re('[-+]?[0-9]*\.?[0-9]+\s')
	   row5= hxs.select('//tr[3]/td[2]/text()').extract()
           row6= hxs.select('//tr[3]/td[3]/text()').extract()
           row7= hxs.select('//tr[3]/td[4]/text()').re('[-+]?[0-9]*\.?[0-9]+\s')
	   row8= hxs.select('//tr[4]/td[2]/text()').extract()
           row9= hxs.select('//tr[4]/td[3]/text()').extract()
           row10= hxs.select('//tr[4]/td[4]/text()').re('[-+]?[0-9]*\.?[0-9]+\s')
	   row11= hxs.select('//tr[5]/td[2]/text()').extract()
           row12= hxs.select('//tr[5]/td[3]/text()').extract()
           row13= hxs.select('//tr[5]/td[4]/text()').re('[-+]?[0-9]*\.?[0-9]+\s')
	   row14= hxs.select('//tr[6]/td[2]/text()').extract()
           row15= hxs.select('//tr[6]/td[3]/text()').extract()
           row16= hxs.select('//tr[6]/td[4]/text()').re('[-+]?[0-9]*\.?[0-9]+\s')
	   row17= hxs.select('//tr[7]/td[2]/text()').extract()
           row18= hxs.select('//tr[7]/td[3]/text()').extract()
           row19= hxs.select('//tr[7]/td[4]/text()').re('[-+]?[0-9]*\.?[0-9]+\s')
	   row20= hxs.select('//tr[8]/td[2]/text()').extract()
           row21= hxs.select('//tr[8]/td[3]/text()').extract()
           row22= hxs.select('//tr[8]/td[4]/text()').re('[-+]?[0-9]*\.?[0-9]+\s')
	   row23= hxs.select('//tr[9]/td[2]/text()').extract()
           row24= hxs.select('//tr[9]/td[3]/text()').extract()
           row25= hxs.select('//tr[9]/td[4]/text()').re('[-+]?[0-9]*\.?[0-9]+\s')
	   row26= hxs.select('//tr[10]/td[2]/text()').extract()
           row27= hxs.select('//tr[10]/td[3]/text()').extract()
           row28= hxs.select('//tr[10]/td[4]/text()').re('[-+]?[0-9]*\.?[0-9]+\s')
	   row29= hxs.select('//tr[11]/td[2]/text()').extract()
           row30= hxs.select('//tr[11]/td[3]/text()').extract()           
	   row31= hxs.select('//tr[11]/td[4]/text()').re('[-+]?[0-9]*\.?[0-9]+\s')  
	   item['col1'] = row1
           item['col2'] = row2
           item['col3'] = row3
           item['col4'] = row4
           item['col5'] = row5
           item['col6'] = row6
           item['col7'] = row7
           item['col8'] = row8
           item['col9'] = row9
           item['col10'] = row10
           item['col11'] = row11
           item['col12'] = row12
           item['col13'] = row13
           item['col14'] = row14
           item['col15'] = row15
           item['col16'] = row16
           item['col17'] = row17
           item['col18'] = row18
           item['col19'] = row19
           item['col20'] = row20
           item['col21'] = row21
           item['col22'] = row22
           item['col23'] = row23
           item['col24'] = row24
           item['col25'] = row25
           item['col26'] = row26
           item['col27'] = row27
           item['col28'] = row28
           item['col29'] = row29
           item['col30'] = row30
           item['col31'] = row31
           items.append(item)
           return items
